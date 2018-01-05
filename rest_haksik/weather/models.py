from django.db import models


class Weather(models.Model):
    temp = models.FloatField()

    def __str__(self):
        return "온도 : {}˚ c".format(self.temp)
