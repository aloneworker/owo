from django.db import models
from datetime import datetime
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=4)
    describe = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class charact(models.Model):
    normalDescription = models.CharField(max_length=40)
    sexMDescription = models.CharField(max_length=40)
    ntrMDescription = models.CharField(max_length=40)
    happyDescription = models.CharField(max_length=40)
    angryDescription = models.CharField(max_length=40)
    hightDescription = models.CharField(max_length=40)
    sexFDescription = models.CharField(max_length=40)
    ntrFDescription = models.CharField(max_length=40)
    keyWord = models.CharField(max_length=10)
    def __str__(self):
        return self.keyWord

class toDomodel(models.Model):
    text_data = models.CharField(max_length=30)
    bool_data = models.BooleanField()


class bulletNotemodel(models.Model):
 
    title = models.CharField(max_length=2)
    content = models.TextField()
    date = models.DateField(null=True, blank=True)
    done = models.CharField(max_length=1)
    txt = models.TextField( default='', blank=True)
    order = models.CharField(max_length=3,default=0)
    tags = models.ManyToManyField(Tag)
    checkDa = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title


