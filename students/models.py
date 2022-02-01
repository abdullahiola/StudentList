from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Student(models.Model):

  gender_choices = [
    ('M','Male'),
    ('F','Female'),

  ]

  grade_choices= [
    ('A','Excellent'),
    ('B','Very_good'),
    ('C','Average'),
    ('D','Pass'),
    ('E','Lower_Pass'),
    ('F','Fail'),
  ]


  Roll_id = models.IntegerField(unique=True, primary_key=True, editable=False,auto_created=True)
  Photo= models.ImageField(upload_to='photos')
  Fullname = models.CharField(max_length=200)
  Course= models.CharField(max_length=200)
  Grade= models.CharField(choices=grade_choices,max_length=100)
  Gender= models.CharField(choices=gender_choices,max_length=20)

  def __str__(self):
    return self.Fullname
  


  