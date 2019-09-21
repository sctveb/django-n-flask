from django.db import models
from django.urls import reverse
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    answerA = models.CharField(max_length=100)
    answerB = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('questions:index')