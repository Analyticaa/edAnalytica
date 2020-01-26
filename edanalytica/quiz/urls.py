from django.urls import path
from quiz.views import QuizDetailView, ReviewView, ViewStepsView, QuizStartView

urlpatterns = [
      path(r's/quiz/<uuid:submission_uuid>/review/', ReviewView.as_view()),
      path(r's/quiz/<uuid:submission_uuid>/', QuizDetailView.as_view(), name='quiz-submission'),
      path(r's/quiz/start/', QuizStartView.as_view()),
      path(r's/quiz/steps/', ViewStepsView.as_view()),
]