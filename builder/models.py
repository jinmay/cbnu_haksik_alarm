from django.db import models


class Info(models.Model):
    user_key = models.CharField(verbose_name="유저식별키", max_length=50)
    dorm = models.CharField(verbose_name="기숙사", max_length=10)

    def __str__(self):
        return self.user_key


class CentralDorm(models.Model):
    day = models.IntegerField()
    menu = models.TextField(max_length=200)

    def __str__(self):
        return "본관 - {}".format(self.day)


class Yangsung(models.Model):
    day = models.IntegerField()
    menu = models.TextField(max_length=200)

    def __str__(self):
        return "양성재 - {}".format(self.day)


class Yangjin(models.Model):
    day = models.IntegerField()
    menu = models.TextField(max_length=200)

    def __str__(self):
        return "양진재 - {}".format(self.day)
