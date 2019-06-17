import datetime
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Main, Yangsung, Yangjin
from .serializers import TodayMenuSerializer


def today():
    date = datetime.datetime.now().isoweekday() # isoweekday는 월요일이 1부터 시작
    return date

def get_day(date):
    week_list = ['월요일', '화요일', '수요일' ,'목요일', '금요일', '토요일', '일요일']
    week = {
        idx: v
        for idx, v in enumerate(week_list, 1)
    }
    return week[date]
    

@api_view(['GET'])
def get_today(request, format=None):
    today_main = get_object_or_404(Main, day=today())
    serializer_main = TodayMenuSerializer(today_main)

    today_yangsung = get_object_or_404(Yangsung, day=today())
    serializer_yangsung = TodayMenuSerializer(today_yangsung)

    today_yangjin = get_object_or_404(Yangjin, day=today())
    serializer_yangjin = TodayMenuSerializer(today_yangjin)

    data = {
        "day": get_day(today()),
        "main": serializer_main.data,
        "yangsung": serializer_yangsung.data,
        "yangjin": serializer_yangjin.data
    }
    return Response(data=data, status=status.HTTP_200_OK)