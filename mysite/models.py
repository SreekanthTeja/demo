from django.db import models
from datetime import datetime

# Create your models here.
class Tutorials(models.Model):
    tutorial_name=models.CharField(max_length=200)
    tutorial_content=models.TextField(max_length=200)
    tutorial_published=models.DateTimeField("Date Published",default=datetime.now())
    def __str__(self):
        return self.tutorial_name

    