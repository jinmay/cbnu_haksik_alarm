from django.contrib import admin

from .models import (
                Main, Yangjin, Yangsung, Crj,
                Star, Galaxy,
                User,
            )

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['number', 'menu']
    list_display_links = ['menu']


@admin.register(Yangsung)
class YangsungAdmin(admin.ModelAdmin):
    list_display = ['number', 'menu']
    list_display_links = ['menu']


@admin.register(Yangjin)
class YangjinAdmin(admin.ModelAdmin):
    list_display = ['number', 'menu']
    list_display_links = ['menu']


@admin.register(Crj)
class CrjAdmin(admin.ModelAdmin):
    list_display = ['number', 'menu']
    list_display_links = ['menu']


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    pass


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = ['number', 'menu']
    list_display_links = ['menu']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['key', 'dorm']