from django.db import models


class Weather(models.Model):
    temp = models.IntegerField()

    def __str__(self):
        return "온도 : {}˚ c".format(self.temp)
