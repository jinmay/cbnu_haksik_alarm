from rest_framework import serializers
from .models import Main


class TodayMenuSerializer(serializers.Serializer):
    breakfast = serializers.CharField()
    lunch = serializers.CharField()
    dinner = serializers.CharField()

