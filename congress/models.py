from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    district = models.IntegerField(null=True,db_index=True)
    state = models.CharField(max_length=2,null=True,db_index=True)
    contact_page = models.URLField(null=True)
    person_id = models.IntegerField(null=True)
    title = models.CharField(max_length=50,null=True)
    title_long = models.CharField(max_length=100,null=True)
    office_addr = models.CharField(max_length=256,null=True)
    party = models.CharField(max_length=32,null=True)
    twitter_username = models.CharField(max_length=24,null=True)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    district = models.IntegerField()