from django.urls import path
from . import views
from . import crawling


app_name = "builder"

urlpatterns = [
    # skill
    path('set_dorm/', views.set_dorm),
    path('show_days/', views.show_days),
    path('show_menus/', views.show_menus),

    # crawling
    path('centraldorm/', crawling.central),
    path('yangsung/', crawling.yangsung),
    path('yangjin/', crawling.yangjin),
]