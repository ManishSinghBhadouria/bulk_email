from django.db import models
from django.utils import timezone

# Create your models here.
class registration(models.Model):
    name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    programme=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    sem=models.CharField(max_length=100)
    currentdate= models.DateField(default=timezone.now)

    def __str__(self):
        return self.email