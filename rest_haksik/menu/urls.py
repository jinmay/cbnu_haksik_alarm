from django.conf.urls import url

from . import views
from . import crawling

urlpatterns = [
    # crawling
    url(r'^main.crawling$', crawling.main_crawling, name="main_crawling"),
    url(r'^jin.crawling$', crawling.jin_crawling, name="jin_crawling"),
    url(r'^sung.crawling$', crawling.sung_crawling, name="sung_crawling"),
    url(r'^crj.crawling$', crawling.crj_crawling, name="crj_crawling"),
    url(r'^star.crawling$', crawling.star_crawling, name="star_crawling"),
    url(r'^galaxy.crawling$', crawling.galaxy_crawling, name="galaxy_crawling"),

    # For Kakaotalk auto reply
    url(r'^keyboard$', views.keyboard, name="keyboard"),
    url(r'^message$', views.Answer.as_view(), name="answer"),
    url(r'^friend$', views.Friend.as_view(), name="friends"),
    url(r'^leave$', views.leave_chatroom, name="chatroom"),
]
