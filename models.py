from django.db import models

# Create your models here.
class Cricketer(models.Model):
	name = models.CharField( max_length=50)
	age = models.IntegerField()
	address = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	occupation = models.CharField(max_length=50)