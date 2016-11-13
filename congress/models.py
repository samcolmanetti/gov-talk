from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Representative(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    district = models.IntegerField()
    
    
class Senator(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    
    
class UserProfile(models.Model):
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    district = models.IntegerField()