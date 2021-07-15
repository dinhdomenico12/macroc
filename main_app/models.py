from django.db import models
from django.contrib.auth.models import User
class Goals(models.Model):
      calories= models.IntegerField()
      protein=models.IntegerField()
      carbohydrates= models.IntegerField()
      fats= models.IntegerField()
      user = models.ForeignKey(User, on_delete=models.CASCADE)
class Macros(models.Model):
      name= models.CharField(max_length=100)
      calories= models.IntegerField()
      protein=models.IntegerField()
      carbohydrates= models.IntegerField()
      fats= models.IntegerField()
      user = models.ForeignKey(User, on_delete=models.CASCADE)



