from django.db import models
from django.utils.functional import cached_property
from django.contrib.auth.models import User

from common.models import BaseModel, UUIDModel
from org.models import Org


class QuestionType(UUIDModel):

    name = models.CharField(max_length=50, unique=True,
                            null=False, blank=False)

    class Meta:
        pass


class QuestionPool(BaseModel):

    question = models.TextField(max_length=4000, null=False, blank=False)
    question_type = models.ForeignKey(
        QuestionType, on_delete=models.DO_NOTHING, default=1)
    tags = models.CharField(max_length=10, blank=True,
                            null=True)  # TODO: will consider later
    explanation = models.TextField(max_length=4000, null=True, blank=True)

    @cached_property
    def options(self):
        return self.mcqoptions_set.all()

    def validate(self, submitted_answer):
        actual_answer = self.mcqoptions_set.get(is_answer=True).pk
        return actual_answer == submitted_answer

    class Meta:
        pass


class MCQOptions(BaseModel):

    question = models.ForeignKey(QuestionPool, on_delete=models.DO_NOTHING)
    option = models.TextField(max_length=4000, null=False)
    is_answer = models.BooleanField(default=False)

    class Meta:
        pass


class Quiz(BaseModel):

    org = models.ForeignKey(Org, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=False)
    questions = models.ManyToManyField(QuestionPool)
    duration = models.IntegerField(default=60)

    class Meta:
        pass

    @cached_property
    def question_ids(self):
        return self.questions.values_list('id', flat=True)

    @cached_property
    def num_of_questions(self):
        return self.questions.all().count()


class QuizSubmissionCache(UUIDModel):

    pass



class SubmissionMeta(UUIDModel):

    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    submitted_on = models.DateTimeField(null=True)
    started_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_completed(self):
        return self.submitted_on is not None

    @property
    def time_taken(self):
        diff = self.submitted_on - self.started_at
        total_seconds = diff.seconds
        hours = total_seconds//3600
        minutes = (total_seconds%3600)//60
        seconds = (total_seconds%3600)%60
        return '{:02d}:{:02d}:{}'.format(hours, minutes, seconds)

    @cached_property
    def num_of_errors(self):
        return self.submissions_set.filter(is_correct=False).count()

    class Meta:
        pass


class Submissions(UUIDModel):

    question = models.ForeignKey(QuestionPool, on_delete=models.DO_NOTHING)
    answer = models.PositiveIntegerField()
    submission = models.ForeignKey(SubmissionMeta, on_delete=models.DO_NOTHING)
    is_correct = models.BooleanField(default=False)

    @cached_property
    def correct_answer(self):
        return self.question.answer

    @cached_property
    def wrong_answer(self):
        pass

    class Meta:
        pass
