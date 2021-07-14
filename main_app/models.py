from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

class Goals(models.Model):
      calories= models.FloatField(max_length=10)
      protein=models.FloatField(max_length= 4)
      carbohydrates= models.FloatField(max_length= 4)
      fats= models.FloatField(max_length=4)   
      user = models.ForeignKey(User, on_delete=models.CASCADE)

class Macros(models.Model):
      name= models.CharField(max_length=100)
      calories= models.FloatField(max_length=10)
      protein=models.FloatField(max_length= 4)
      carbohydrates= models.FloatField(max_length= 4)
      fats= models.FloatField(max_length=4)
      goals = models.ForeignKey(Goals, on_delete=models.CASCADE)
      



