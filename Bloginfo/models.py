from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    blogtext = models.TextField(max_length=100000)
    date = models.DateField(auto_created=True)
