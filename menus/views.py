import datetime

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
                Main, Yangjin, Yangsung,
                User,
            )
from .serializers import MenuSerializer


INIT_KEYBOARD = ['중문기숙사', '양진재', '양성재']
DORM_WEEKDAY = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일', '기숙사 선택']
UNIDORM = ['중문기숙사', '양진재', '양성재']

@api_view(['GET'])
def keyboard(request):
    keyboard = {
        "type": "buttons",
        "buttons": INIT_KEYBOARD
    }

    return Response(data=keyboard, status=status.HTTP_200_OK)


class Answer(APIView):

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
        day_dict = {key: index for index, key in enumerate(DORM_WEEKDAY, 1)}
        day_dict['일요일'] = 0

        if dorm == "중문기숙사":
            return Main.objects.get(number=day_dict[weekday])
        elif dorm == "양성재":
            return Yangsung.objects.get(number=day_dict[weekday])
        elif dorm == "양진재":
            return Yangjin.objects.get(number=day_dict[weekday])

    # 키보드 응답할때
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

    # 텍스트 응답할때
    def show_text(self):
        response = {
            "message": {
                "text": None
            }
        }
        return response

    def get_user(self, key):
        try:
            user = User.objects.get(key=key)
        except User.DoesNotExist:
            user = User.objects.create(key=key)
        return user

    def post(self, request, format=None):
        rawdata = self.request.data
        user_key = rawdata.get("user_key", None)
        content = rawdata.get("content", None)
        user = self.get_user(user_key)

        # 기숙사의 종류를 선택했을 때
        if content in UNIDORM:
            user.dorm = content
            user.save()

            keyboard = self.show_keyboard(DORM_WEEKDAY)
            keyboard["message"]["text"] = content + "\n\n" + self.today_date()

            return Response(keyboard, status=status.HTTP_200_OK)

        # "기숙사 선택"을 눌렀을때 -> 처음으로 돌아갔을때와 같은 키보드를 출력한다
        elif content == "기숙사 선택":
            keyboard = self.show_keyboard(INIT_KEYBOARD)
            keyboard["message"]["text"] = content

            return Response(keyboard, status=status.HTTP_200_OK)

        # 요일 선택시
        elif content in DORM_WEEKDAY:
            dorm = user.dorm

            if dorm in UNIDORM:
                dorm_menu = self.show_menu(dorm, content)    
                keyboard = self.show_keyboard(DORM_WEEKDAY)

            serializer = MenuSerializer(dorm_menu)
            keyboard["message"] = serializer.data

            return Response(keyboard, status=status.HTTP_200_OK)

        # 처음으로 입력했을 때
        elif content == "처음으로":
            ment = "처음으로 돌아갈게욤~@"
            keyboard = self.show_keyboard(INIT_KEYBOARD)
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
