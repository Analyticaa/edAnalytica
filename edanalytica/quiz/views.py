from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from datetime import datetime

from quiz.models import QuestionPool, MCQOptions, QuestionType, Quiz, SubmissionMeta, Submissions


class QuizDetailView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs['quiz_id']
        # print(pk)
        quiz = get_object_or_404(Quiz, pk=int(pk))
        # quiz = Quiz.objects.all().first()
        page = request.GET.get('page') or 1
        questions = quiz.questions.all()
        paginator = Paginator(questions, 2)
        questions = paginator.get_page(page)
        test_date = datetime.now()

        context = {
            'quiz': quiz,
            'questions': questions,
            'page': page,
            'paginator': paginator,
            'test_date': test_date
        }
        return render(request, "quiz/quiz.html", status=200, context=context)


class ReviewView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs['quiz_id']
        user = request.user
        # print(pk)
        quiz = get_object_or_404(Quiz, pk=int(pk))
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
