from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Person(models.Model):
#   user = models.OneToOneField(User, unique=True, related_name='person')

class Day(models.Model):

  # metadata
  user = models.ForeignKey(User, related_name='days')
  date = models.DateField()

  # virtues
  temperance = models.IntegerField(default=-1)
  silence = models.IntegerField(default=-1)
  order = models.IntegerField(default=-1)
  resolution = models.IntegerField(default=-1)
  frugality = models.IntegerField(default=-1)
  industry = models.IntegerField(default=-1)
  sincerity = models.IntegerField(default=-1)
  justice = models.IntegerField(default=-1)
  moderation = models.IntegerField(default=-1)
  cleanliness = models.IntegerField(default=-1)
  tranquillity = models.IntegerField(default=-1)
  chastity = models.IntegerField(default=-1)
  humility = models.IntegerField(default=-1)
