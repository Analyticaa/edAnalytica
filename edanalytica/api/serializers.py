from rest_framework import serializers
from quiz.models import QuestionPool, Submissions, SubmissionMeta


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionPool
        fields = '__all__'

class SubmissionMetaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubmissionMeta
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submissions
        fields = '__all__'