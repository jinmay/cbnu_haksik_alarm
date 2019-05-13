from django.urls import path
from . import views

app_name = "rn"

urlpatterns = [
    path('get_today/', views.get_today),
]