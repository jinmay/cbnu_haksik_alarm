from django.contrib import admin
from .models import Main, Yangsung, Yangjin

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('display_day', 'breakfast', 'lunch' ,'dinner', )


@admin.register(Yangsung)
class MainAdmin(admin.ModelAdmin):
    list_display = ('display_day', 'breakfast', 'lunch' ,'dinner', )


@admin.register(Yangjin)
class MainAdmin(admin.ModelAdmin):
    list_display = ('display_day', 'breakfast', 'lunch' ,'dinner', )