from statistics import mode
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Identification(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.title