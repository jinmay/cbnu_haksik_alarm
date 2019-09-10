from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menus/', include('menus.urls')),
    path('rn/', include('rn_api.urls')),
    path('builder/', include('builder.urls')),
]
