from django.urls import path
from . import views
from . import crawling

app_name = "rn"

urlpatterns = [
    # For RN api
    path('get_today/', views.get_today),

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
        route='crawling.yangsung',
        view=crawling.sung_crawling,
        name='sung_crawling'
    ),
]