from django.db import models


class Weather(models.Model):
    temp = models.FloatField()
    humidity = models.IntegerField()
    clouds = models.IntegerField()

    def __str__(self):
        return "온도 : {}˚ c / 습도 : {}% / 구름: {}%".format(self.temp, self.humidity, self.clouds)
