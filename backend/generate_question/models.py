from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class InterviewQuestion(models.Model):
    skill = models.CharField(max_length=255)
    question = models.TextField()

    def __str__(self):
        return self.skill

