from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import QuestionSerializer, SubmissionMetaSerializer
from quiz.models import QuestionPool, QuestionType, MCQOptions, SubmissionMeta, Quiz, Submissions
from django.db import transaction
from django.shortcuts import get_object_or_404

from datetime import datetime


class QuestionViewset(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = QuestionPool.objects.all()

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        options = data.pop('options')
        serailizer = self.get_serializer(data=data)
        serailizer.is_valid()
        question = serailizer.save()
        for option, is_answer in options.items():
            MCQOptions.objects.create(
                question=question, option=option, is_answer=is_answer)
        return Response(status=200)


class SubmissionViewset(viewsets.ModelViewSet):
    serializer_class = SubmissionMetaSerializer
    queryset = SubmissionMeta.objects.all()

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        submission_uuid = data.pop('submission_uuid')
        submission_meta = get_object_or_404(
            SubmissionMeta, uuid=submission_uuid)
        quiz = submission_meta.quiz
        data['quiz'] = quiz.pk
        data['user'] = request.user.pk
        data['submitted_on'] = datetime.now()
        actual_question_ids = quiz.question_ids
        answers = data.pop('answers')
        answered_question_ids = [int(ans['question_id']) for ans in answers]
        if set(actual_question_ids) != set(answered_question_ids):
            return Response({
                'message': 'Please answer all questions'
            }, status=400)

        serializer = self.get_serializer(submission_meta, data=data)
        serializer.is_valid(raise_exception=True)
        submission_meta = serializer.save()

        submissions = []
        for answer in answers:
            question = QuestionPool.objects.get(pk=answer['question_id'])
            ans = int(answer['answer'])
            submissions.append(Submissions(submission=submission_meta,
                                           question=question, answer=ans, is_correct=question.validate(ans)))
        Submissions.objects.bulk_create(submissions)
        return Response(status=200)
