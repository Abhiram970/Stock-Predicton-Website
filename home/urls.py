from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'about-us'),
    path('home/logout',views.logout,name = 'logout')
]
