from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users (models.Model):
	 UserName= models.CharField(max_length=50)
	 Email = models.EmailField()
	 
