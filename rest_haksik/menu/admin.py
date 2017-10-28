from django.contrib import admin

from .models import Main, Yangjin, Yangsung, Crj

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['number', 'day']
    list_display_links = ['day']


@admin.register(Yangsung)
class YangsungAdmin(admin.ModelAdmin):
    list_display = ['number', 'day']
    list_display_links = ['day']


@admin.register(Yangjin)
class YangjinAdmin(admin.ModelAdmin):
    list_display = ['number', 'day']
    list_display_links = ['day']


@admin.register(Crj)
class CrjAdmin(admin.ModelAdmin):
    list_display = ['number', 'day']
    list_display_links = ['day']
