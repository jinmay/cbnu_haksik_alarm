from django.contrib import admin
from .models import Info, CentralDorm, Yangsung, Yangjin


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('user_key', 'dorm', )


@admin.register(CentralDorm)
class CenteralDormAdmin(admin.ModelAdmin):
    list_display = ('day', 'menu', )
    list_display_links = ('menu', )


@admin.register(Yangsung)
class YangsungAdmin(admin.ModelAdmin):
    list_display = ('day', 'menu', )
    list_display_links = ('menu', )


@admin.register(Yangjin)
class YangjinAdmin(admin.ModelAdmin):
    list_display = ('day', 'menu', )
    list_display_links = ('menu', )