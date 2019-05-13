from rest_framework import serializers
from .models import Main


class TodayMenuSerializer(serializers.Serializer):
    day = serializers.IntegerField()
    breakfast = serializers.CharField()
    lunch = serializers.CharField()
    dinner = serializers.CharField()

