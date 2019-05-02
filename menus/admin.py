from django.contrib import admin
from .models import (
                Main, Yangjin, Yangsung,
                User,
            )

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ['number', 'day', 'menu', ]
    list_display_links = ['day', ]


@admin.register(Yangsung)
class YangsungAdmin(admin.ModelAdmin):
    list_display = ['number', 'day', 'menu', ]
    list_display_links = ['day', ]


@admin.register(Yangjin)
class YangjinAdmin(admin.ModelAdmin):
    list_display = ['number', 'day', 'menu', ]
    list_display_links = ['day', ]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['key', 'dorm']