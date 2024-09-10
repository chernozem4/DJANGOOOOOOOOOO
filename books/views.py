from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    return HttpResponse("Информация обо мне: Ваше имя, возраст, увлечения.")

def about_friend(request):
    return HttpResponse("Информация о друге: Имя друга, возраст, увлечения.")

def current_time(request):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")

