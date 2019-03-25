from django.urls import path
from . import crawling

app_name = 'menus'

urlpatterns = [
    # For crawling
    path(
        route='crawling.main',
        view=crawling.middle_crawling,
        name='middle_crawling'
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