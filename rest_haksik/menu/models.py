from django.db import models

class Main(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return self.menu


class Yangsung(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return self.menu


class Yangjin(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return self.menu


class Crj(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return self.menu


class Star(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return self.menu


class Galaxy(models.Model):
    number = models.IntegerField()
    menu = models.TextField()

    def __str__(self):
        return self.menu

class User(models.Model):
    key = models.CharField(max_length=100)
    dorm = models.CharField(max_length=50, default="", null=True, blank=True)

    def __str__(self):
        return "secretKey: {}".format(self.key)