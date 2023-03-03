from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'sport_app'
urlpatterns = [
    path('sport/',views.SportView.as_view(), name='sport'),
    path('sport_detail/<slug>',views.SportDetail.as_view(), name='sport_detail'),
   
]