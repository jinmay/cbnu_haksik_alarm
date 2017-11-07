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
    menu = models.TextField()

    def __str__(self):
        return self.menu
