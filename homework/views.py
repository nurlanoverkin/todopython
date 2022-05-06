from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

from .models import ToMeet

def homework(request):
    return render(request, "homework.html")

def homework2 (request):
    return HttpResponse("Добро пожаловать в приложение ToDo - Admin")

def meeting(request):
    meet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"meet_list":meet_list})
