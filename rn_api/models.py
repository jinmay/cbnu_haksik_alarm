from django.db import models

class Main(models.Model):
    day = models.IntegerField()
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)