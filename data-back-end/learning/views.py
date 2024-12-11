from django.shortcuts import render
from rest_framework import viewsets

from .models import LearningTopic
from .serializers import LearningTopicSerializer

class LearningTopicViewset(viewsets.ModelViewSet):
    queryset = LearningTopic.objects.all()
    serializer_class = LearningTopicSerializer
