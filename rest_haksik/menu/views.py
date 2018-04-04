import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
                Main, Yangjin, Yangsung, Crj,
                Star, Galaxy,
                User
            )
from rest_haksik.weather import models as weather_models
from .serializers import MenuSerializer
from rest_haksik.weather import serializers as weather_serializers


@api_view(['GET'])
def keyboard(request):
    keyboard = {
        "type": "buttons",
        "buttons": ['중문기숙사', '양진재', '양성재', '청람재', '별빛식당', '은하수식당', '현재날씨']
    }
    return Response(data=keyboard, status=status.HTTP_200_OK)


class Answer(APIView):
    unidorm = ['중문기숙사', '양진재', '양성재', '청람재']
    newhall = ['별빛식당', '은하수식당']
    week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일', '기숙사 선택']
    newhall_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '기숙사 선택']
    temp_now = ['현재날씨']

    # 오늘이 몇 일 무슨 요일인지 문자열로 리턴
    def today_date(self):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        date = datetime.datetime.now().weekday()
        date_list = ('월', '화', '수', '목', '금', '토', '일')
        today_str = "오늘은 {}년 {}월 {}일\n{}요일 입니다.".format(year, month, day, date_list[date])

        return today_str

    # 기숙사별 해당 요일 메뉴 리턴
    def show_menu(self, dorm, weekday):
        '''
            학교기숙사와 청람재의 경우 월요일: 1 / 일요일: 0
        '''
        day_dict = {key: index for index, key in enumerate(Answer.week, 1)}
        day_dict['일요일'] = 0
        # if dorm == "은하수식당":
        #     day_dict = {key: index for index, key in enumerate(Answer.newhall_week, 0)}

        if dorm == "중문기숙사":
            return Main.objects.get(number=day_dict[weekday])
        elif dorm == "양성재":
            return Yangsung.objects.get(number=day_dict[weekday])
        elif dorm == "양진재":
            return Yangjin.objects.get(number=day_dict[weekday])
        elif dorm == "청람재":
            return Crj.objects.get(number=day_dict[weekday])
        # elif dorm == "은하수식당":
        #     return Galaxy.objects.get(number=day_dict[weekday])

    def show_menu_haksik(self, dorm, weekday):
        '''
            학식과 기숙사 분리
            기숙사는 월 ~ 일 / 학식은 월 ~ 금 이기때문에 분리함
            월요일: 1 / 금요일: 5
        '''
        day_dict = {key: index for index, key in enumerate(Answer.newhall_week, 1)}
        if dorm == "별빛식당":
            return Star.objects.get(number=day_dict[weekday])

    def show_keyboard(self, keyboard_buttons):
        keyboard = {
            "message": {
                "text": None
            },
            "keyboard": {
                "type": "buttons",
                "buttons": keyboard_buttons
            }
        }
        return keyboard

    def get_user(self, key):
        try:
            user = User.objects.get(key=key)
        except User.DoesNotExist:
            user = User.objects.create(key=key)
        return user

    def get_temp(self):
        temp = float(weather_models.Weather.objects.last().temp)
        humidity = int(weather_models.Weather.objects.last().humidity)
        clouds = int(weather_models.Weather.objects.last().clouds)

        return (temp, humidity, clouds)

    def post(self, request, format=None):
        rawdata = self.request.data
        user_key = rawdata.get("user_key", None)
        content = rawdata.get("content", None)

        user = self.get_user(user_key)

        # 기숙사의 종류를 선택했을 때
        if content in Answer.unidorm:
            # Answer.selected_dorm = content
            user.dorm = content
            user.save()

            keyboard = self.show_keyboard(Answer.week)
            keyboard["message"]["text"] = content + "\n\n" + self.today_date()

            return Response(keyboard, status=status.HTTP_200_OK)
        # 별빛식당 선택시
        elif content == "별빛식당":
            user.dorm = content
            user.save()

            keyboard = self.show_keyboard(Answer.newhall_week)
            keyboard["message"]["text"] = content + "\n\n" + self.today_date()

            return Response(keyboard, status=status.HTTP_200_OK)
        # 별빛식당을 제외한 신학생회관 - 은하수식당, 한빛식당 선택 시
        # elif content in Answer.newhall:
        #     user.dorm = content
        #     user.save()

        #     keyboard = self.show_keyboard(Answer.newhall_week)
        #     keyboard["message"]["text"] = content + "\n\n" + self.today_date()

        #     return Response(keyboard, status=status.HTTP_200_OK)
        # "기숙사 선택"을 눌렀을때
        elif content == "기숙사 선택":
            keyboard = self.show_keyboard(Answer.unidorm + Answer.newhall + Answer.temp_now)
            keyboard["message"]["text"] = content

            return Response(keyboard, status=status.HTTP_200_OK)
        # 요일 선택시
        elif content in Answer.week:
            dorm = user.dorm
            if dorm in Answer.unidorm:
                dorm_menu = self.show_menu(dorm, content)    
                keyboard = self.show_keyboard(Answer.week)
            elif dorm in Answer.newhall:
                dorm_menu = self.show_menu_haksik(dorm, content)
                keyboard = self.show_keyboard(Answer.newhall_week)

            serializer = MenuSerializer(dorm_menu)
            keyboard["message"] = serializer.data

            return Response(keyboard, status=status.HTTP_200_OK)
        # 현재날씨 선택시
        elif content == "현재날씨":
            temp, humidity, clouds = self.get_temp()
            ment = """현재 청주시의 날씨는 \n *온도: {}˚c\n *습도: {}%\n *흐림: {}%\n입니다.""".format(temp, humidity, clouds)
            keyboard = self.show_keyboard(Answer.unidorm + Answer.newhall + Answer.temp_now)
            keyboard["message"]["text"] = ment

            return Response(keyboard, status=status.HTTP_200_OK)


# 친구 추가 / 삭제
class Friend(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


# 채팅방 나가기
@api_view(['DELETE'])
def leave_chatroom(request):
    return Response(status=status.HTTP_204_NO_CONTENT)
