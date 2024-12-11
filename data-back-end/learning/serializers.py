from rest_framework import serializers
from .models import LearningTopic, LearningQuestion

class LearningTopicSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    def get_questions(self, obj):
        questions = LearningQuestion.objects.filter(topic=obj)
        return LearningQuestionSerializer(questions, many=True).data

    class Meta:
        model = LearningTopic
        fields = ['name', 'description', 'questions']

class LearningQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningQuestion
        fields = ['topic', 'type', 'question', 'description', 'answerList', 'key']