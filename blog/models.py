"""https://docs.djangoproject.com/en/1.11/ref/models/ """
from django.db import models

# Create your models here.
class Blog (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField( max_length=100)
    blog = models.TextField()

    def __str__(self):
        return self.title
