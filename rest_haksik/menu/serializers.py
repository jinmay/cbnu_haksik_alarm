from rest_framework import serializers
from .models import (
                Main, Yangjin, Yangsung, Crj,
                Notice,
            )


class MenuSerializer(serializers.Serializer):
    text = serializers.CharField(source="menu")


class NoticeSerializer(serializers.Serializer):
    notice = serializers.CharField()
    url = serializers.CharField()