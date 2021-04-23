from django.db import models
#from djangotoolbox.fields import ListField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=1000)
    date = models.DateField()
    tags = models.CharField(max_length=100)

def __str__(self):
    return self.title
