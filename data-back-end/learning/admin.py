from django.contrib import admin
from .models import LearningTopic, LearningQuestion

admin.site.register(LearningTopic)
admin.site.register(LearningQuestion)
