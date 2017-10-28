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
    week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    selected_dorm = ""

    def post(self, request, format=None):
        rawdata = self.request.data
        user_key = rawdata.get("user_key", None)
        content = rawdata.get("content", None)

        # 기숙사별 해당 요일 메뉴 리턴
        def show_menu(dorm, weekday):
            day_dict = {key: index for index, key in enumerate(Answer.week, 1)}
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

        # 기숙사 선택시
        if content in Answer.dorm:
            Answer.selected_dorm = content
            keyboard = {
                "message": content,
                "keyboard": Answer.week
            }
            return Response(keyboard, status=status.HTTP_200_OK)
        # 요일 선택시
        elif content in Answer.week:
            menu = show_menu(Answer.selected_dorm, content)
            serializer = MenuSerializer(menu)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
