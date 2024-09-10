from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me, name='about_me'),
    path('about_friend/', views.about_friend, name='about_friend'),
    path('current_time/', views.current_time, name='current_time'),
]
