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
        "buttons": ['중문기숙사', '양진재', '양성재', '청람재', '별빛식당', '은하수식당']
    }
    return Response(data=keyboard, status=status.HTTP_200_OK)


class Answer(APIView):
    unidorm = ['중문기숙사', '양진재', '양성재', '청람재']
    newhall = ['별빛식당', '은하수식당']
    week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일', '기숙사 선택']
    newhall_week = ['월요일', '화요일', '수요일', '목요일', '금요일', '기숙사 선택']
    temp_now = ['현재기온']

    # 오늘이 몇 일 무슨 요일인지 문자열로 리턴
    def today_date(self):
        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        date = datetime.datetime.now().weekday()
        date_list = ['월', '화', '수', '목', '금', '토', '일']

        today_str = "오늘은 {}년 {}월 {}일\n{}요일 입니다.".format(year, month, day, date_list[date])

        return today_str


    # 기숙사별 해당 요일 메뉴 리턴
    def show_menu(self, dorm, weekday):
        '''
            청람재와 신학생회관의 경우 월요일: 0 / 일요일: 6
            학교기숙사의 경우 월요일: 1 / 일요일: 0
        '''
        day_dict = {key: index for index, key in enumerate(Answer.week, 1)}
        day_dict['일요일'] = 0
        if dorm == "청람재" or dorm == "은하수식당":
            day_dict = {key: index for index, key in enumerate(Answer.week, 0)}

        if dorm == "중문기숙사":
            return Main.objects.get(number=day_dict[weekday])
        elif dorm == "양성재":
            return Yangsung.objects.get(number=day_dict[weekday])
        elif dorm == "양진재":
            return Yangjin.objects.get(number=day_dict[weekday])
        elif dorm == "청람재":
            return Crj.objects.get(number=day_dict[weekday])
        elif dorm == "은하수식당":
            return Galaxy.objects.get(number=day_dict[weekday])

    # 신학생회관 메뉴 리턴
    def show_newhall(self, sort):
        if sort == "별빛식당":
            menu = Star.objects.first()
            return menu

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
        return temp

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
            newhall_menu = self.show_newhall(content)
            serializer = MenuSerializer(newhall_menu)
            keyboard = self.show_keyboard(Answer.unidorm + Answer.newhall)
            keyboard["message"] = serializer.data

            return Response(keyboard, status=status.HTTP_200_OK)
        # 별빛식당을 제외한 신학생회관 - 은하수식당, 한빛식당 선택 시
        elif content in Answer.newhall:
            user.dorm = content
            user.save()

            keyboard = self.show_keyboard(Answer.newhall_week)
            keyboard["message"]["text"] = content + "\n\n" + self.today_date()

            return Response(keyboard, status=status.HTTP_200_OK)
        # "기숙사 선택"을 눌렀을때
        elif content == "기숙사 선택":
            keyboard = self.show_keyboard(Answer.unidorm + Answer.newhall + Answer.temp_now)
            keyboard["message"]["text"] = content

            return Response(keyboard, status=status.HTTP_200_OK)
        # 요일 선택시
        elif content in Answer.week:
            dorm = user.dorm
            dorm_menu = self.show_menu(dorm, content)
            serializer = MenuSerializer(dorm_menu)

            keyboard = self.show_keyboard(Answer.week)
            # 은하수식당은 '토요일'과 '일요일'이 보이면 안되기 때문
            # 임시코드 
            if user.dorm == "은하수식당":
                keyboard = self.show_keyboard(Answer.newhall_week)
            keyboard["message"] = serializer.data

            return Response(keyboard, status=status.HTTP_200_OK)
        # 현재기온 선택시
        # elif content == "현재기온":
        #     temp = self.get_temp()
        #     ment = "청주시의 현재 기온은 {}입니다.".format(temp)
        #     keyboard = self.show_keyboard(Answer.unidorm + Answer.newhall + Answer.temp_now)
        #     keyboard["message"]["text"] = ment

        #     return Response(keyboard, status=status.HTTP_200_OK)


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
