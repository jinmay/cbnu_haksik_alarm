from django.db import models

week_list = ['월요일', '화요일', '수요일' ,'목요일', '금요일', '토요일', '일요일']
week = {
    idx: v
    for idx, v in enumerate(week_list, 1)
}

class Main(models.Model):
    day = models.IntegerField()
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()

    def __str__(self):
        return "중문기숙사 - {}".format(week[self.day])

    @property
    def display_day(self):
        return "중문기숙사 - {}".format(week[self.day])


class Yangsung(models.Model):
    day = models.IntegerField()
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()

    def __str__(self):
        return "양성재 - {}".format(week[self.day])

    @property
    def display_day(self):
        return "양성재 - {}".format(week[self.day])

        
class Yangjin(models.Model):
    day = models.IntegerField()
    breakfast = models.TextField()
    lunch = models.TextField()
    dinner = models.TextField()

    def __str__(self):
        return "양진재 - {}".format(week[self.day])

    @property
    def display_day(self):
        return "양진재 - {}".format(week[self.day])