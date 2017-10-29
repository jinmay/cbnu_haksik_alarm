from rest_framework import serializers
from .models import Main, Yangjin, Yangsung, Crj


class MenuSerializer(serializers.Serializer):
    text = serializers.CharField(source="menu")
