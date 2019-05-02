from django.urls import path
from . import views
from . import crawling

app_name = 'menus'

urlpatterns = [
    # For Kakaotalk auto reply
    path('keyboard', views.keyboard, name="keyboard"),
    path('message', views.Answer.as_view(), name="answer"),
    path('friend', views.Friend.as_view(), name="friends"),
    path('leave', views.leave_chatroom, name="chatroom"),

    # For crawling
    path(
        route='crawling.main',
        view=crawling.main_crawling,
        name='main_crawling'
    ),
    path(
        route='crawling.yangjin',
        view=crawling.jin_crawling,
        name='jin_crawling'
    ),
    path(
        route='crawling.main',
        view=crawling.sung_crawling,
        name='sung_crawling'
    ),
]