from django.db import models

class LearningTopic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class LearningQuestion(models.Model):
    topic = models.ForeignKey(LearningTopic, on_delete=models.CASCADE)
    type = models.CharField(null=False, max_length=255)
    question = models.TextField(null=False)
    description = models.TextField()
    answerList = models.JSONField(default=list)
    key = models.JSONField(default=list)

    def __str__(self):
        return self.question
