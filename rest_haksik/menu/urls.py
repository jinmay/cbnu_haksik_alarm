from django.conf.urls import url

from . import crawling

urlpatterns = [
    # crawling
    url(r'^main.crawling$', crawling.main_crawling, name="main_crawling"),
    url(r'^jin.crawling$', crawling.jin_crawling, name="jin_crawling"),
    url(r'^sung.crawling$', crawling.sung_crawling, name="sung_crawling"),
    url(r'^crj.crawling$', crawling.crj_crawling, name="crj_crawling"),
]
