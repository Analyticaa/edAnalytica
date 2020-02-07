from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from datetime import datetime, timedelta


from quiz.models import QuestionPool, MCQOptions, QuestionType, Quiz, SubmissionMeta, Submissions


class QuizDetailView(View):

    def get(self, request, *args, **kwargs):
        submission_uuid = kwargs['submission_uuid']
        # print(pk)
        submission_meta = get_object_or_404(
            SubmissionMeta, uuid=submission_uuid)
        if submission_meta.is_completed:
            return HttpResponse(status=404)
        quiz = submission_meta.quiz
        # quiz = Quiz.objects.all().first()
        page = request.GET.get('page') or 1
        questions = quiz.questions.all()
        paginator = Paginator(questions, 2)
        questions = paginator.get_page(page)
        test_date = datetime.now()
        started_at = submission_meta.started_at + \
            timedelta(minutes=quiz.duration)
        started_at = datetime.strftime(started_at, "%Y-%m-%dT%H:%M:%SZ")

        context = {
            'quiz': quiz,
            'questions': questions,
            'page': page,
            'paginator': paginator,
            'test_date': test_date,
            'started_at': started_at,
            'submission_uuid': submission_uuid
        }
        if request.is_ajax():
            return render(request, "quiz/quiz-body.html", status=200, context=context)
        return render(request, "quiz/quiz.html", status=200, context=context)


class QuizStartView(View):

    def get(self, request, *args, **kwargs):
        # context = {
        #     "quiz_id": 1
        # }
        # return render(request, "quiz/quiz-start.html", status=200, context=context)
        quiz_id = 1
        quiz = get_object_or_404(Quiz, pk=quiz_id, org=request.org)

        user = request.user
        submission_meta = SubmissionMeta.objects.create(
            quiz=quiz, user=user)
        submission_uuid = submission_meta.uuid
        return HttpResponseRedirect(reverse('quiz-submission', kwargs={'submission_uuid': submission_uuid}))

    def post(self, request, *args, **kwargs):
        quiz_id = int(request.POST['quiz-id'])
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        user = request.user
        submission_meta = SubmissionMeta.objects.create(
            quiz=quiz, user=user)
        submission_uuid = submission_meta.uuid
        return HttpResponseRedirect(reverse('quiz-submission', kwargs={'submission_uuid': submission_uuid}))


class ReviewView(View):

    def get(self, request, *args, **kwargs):
        submission_uuid = kwargs['submission_uuid']
        user = request.user
        # print(pk)
        submission_meta = get_object_or_404(
            SubmissionMeta, uuid=submission_uuid)
        quiz = submission_meta.quiz
        page = request.GET.get('page') or 1
        questions = quiz.questions.all()
        paginator = Paginator(questions, 2)
        questions = paginator.get_page(page)

        submission_meta = SubmissionMeta.objects.filter(
            quiz=quiz, user=user).last()
        submissions = Submissions.objects.filter(
            question__in=questions, submission=submission_meta)
        test_date = datetime.now()

        context = {
            'quiz': quiz,
            'questions': questions,
            'page': page,
            'paginator': paginator,
            'submissions': submissions,
            'test_date': test_date,
            'submission_meta': submission_meta
        }
        return render(request, "quiz/quiz-review.html", status=200, context=context)


class ViewStepsView(View):

    def get(self, request, *args, **kwargs):
        pk = request.GET.get('sId') or 0
        qIdx = request.GET.get('qIdx')
        submission = get_object_or_404(Submissions, pk=int(pk))

        context = {
            'submission': submission,
            'qIdx': qIdx
        }

        return render(request, "quiz/view-steps.html", status=200, context=context)
