from django.db import models

week_list = ['일요일', '월요일', '화요일', '수요일' ,'목요일', '금요일', '토요일']
week = {
    idx: v
    for idx, v in enumerate(week_list)
}

class Main(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return "중문기숙사 - {}".format(week[self.number])

    @property
    def day(self):
        return "중문기숙사 - {}".format(week[self.number])


class Yangsung(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return "양성재 - {}".format(week[self.number])

    @property
    def day(self):
        return "양성재 - {}".format(week[self.number])


class Yangjin(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return "양진재 - {}".format(week[self.number])

    @property
    def day(self):
        return "양진재 - {}".format(week[self.number])


class User(models.Model):
    key = models.CharField(max_length=100)
    dorm = models.CharField(max_length=50, default="")