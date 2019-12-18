from django.urls import path
from quiz.views import QuizDetailView, ReviewView

urlpatterns = [
      path(r's/quiz/<int:quiz_id>/review/', ReviewView.as_view()),
      path(r's/quiz/<int:quiz_id>/', QuizDetailView.as_view()),
]