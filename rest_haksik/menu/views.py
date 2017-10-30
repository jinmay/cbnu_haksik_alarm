import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Main, Yangsung, Yangjin, Crj
from .serializers import MenuSerializer


@api_view(['GET'])
def keyboard(request):
    keyboard = {
        "type": "buttons",
        "buttons": ['중문기숙사', '양진재', '양성재', '청람재']
    }
    return Response(data=keyboard, status=status.HTTP_200_OK)


class Answer(APIView):
    dorm = ['중문기숙사', '양진재', '양성재', '청람재']
    week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일', '기숙사 선택']
    selected_dorm = ""

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
        day_dict = {key: index for index, key in enumerate(Answer.week, 1)}
        day_dict['일요일'] = 0
        if dorm == "청람재":
            day_dict = {key: index for index, key in enumerate(Answer.week, 0)}

        if dorm == "중문기숙사":
            return Main.objects.get(number=day_dict[weekday])
        elif dorm == "양성재":
            return Yangsung.objects.get(number=day_dict[weekday])
        elif dorm == "양진재":
            return Yangjin.objects.get(number=day_dict[weekday])
        elif dorm == "청람재":
            return Crj.objects.get(number=day_dict[weekday])

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

    def post(self, request, format=None):
        rawdata = self.request.data
        user_key = rawdata.get("user_key", None)
        content = rawdata.get("content", None)

        # 기숙사의 종류를 선택했을 때
        if content in Answer.dorm:
            Answer.selected_dorm = content

            keyboard = self.show_keyboard(Answer.week)
            keyboard["message"]["text"] = content + "\n\n" + self.today_date()

            return Response(keyboard, status=status.HTTP_200_OK)
        elif content == "기숙사 선택":
            keyboard = self.show_keyboard(Answer.dorm)
            keyboard["message"]["text"] = content

            return Response(keyboard, status=status.HTTP_200_OK)
        # 요일 선택시
        elif content in Answer.week:
            menu = self.show_menu(Answer.selected_dorm, content)
            serializer = MenuSerializer(menu)

            keyboard = self.show_keyboard(Answer.week)
            keyboard["message"] = serializer.data

            return Response(keyboard, status=status.HTTP_200_OK)


# 친구 추가 / 삭제
class Friend(APIView):
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        return Response(status=status.HTTP_200_OK)


# 채팅방 나가기
@api_view(['DELETE'])
def leave_chatroom(request):
    return Response(status=status.HTTP_200_OK)
