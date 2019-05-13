from django.db import models

week_list = ['일요일', '월요일', '화요일', '수요일' ,'목요일', '금요일', '토요일']
week = {
    idx: v
    for idx, v in enumerate(week_list)
}

class Main(models.Model):
    day = models.IntegerField()
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return "중문기숙사 - {}".format(week[self.day])

    @property
    def display_day(self):
        return "중문기숙사 - {}".format(week[self.day])


class Yangsung(models.Model):
    day = models.IntegerField()
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return "양성재 - {}".format(week[self.day])

    @property
    def display_day(self):
        return "양성재 - {}".format(week[self.day])

        
class Yangjin(models.Model):
    day = models.IntegerField()
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return "양진재 - {}".format(week[self.day])

    @property
    def display_day(self):
        return "양진재 - {}".format(week[self.day])