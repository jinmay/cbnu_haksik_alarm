from rest_framework import serializers
from .models import Main

def get_day(date):
    week_list = ['월요일', '화요일', '수요일' ,'목요일', '금요일', '토요일', '일요일']
    week = {
        idx: v
        for idx, v in enumerate(week_list, 1)
    }
    return week[date]


class TodayMenuSerializer(serializers.Serializer):
    breakfast = serializers.CharField()
    lunch = serializers.CharField()
    dinner = serializers.CharField()


class WeekMenuSerializer(TodayMenuSerializer):
    id = serializers.IntegerField()
    day2 = serializers.CharField()