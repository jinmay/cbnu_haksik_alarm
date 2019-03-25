from django.contrib import admin
from .models import (
                Middle, Yangjin, Yangsung,
                User,
            )

@admin.register(Middle)
class MiddleAdmin(admin.ModelAdmin):
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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['key', 'dorm']