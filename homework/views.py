from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from main.models import ToDo
from main.views import test
from .models import *

def homework(request):
    return render(request, "homework.html")

def homework2 (request):
    return HttpResponse("Добро пожаловать в приложение ToDo - Admin")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def meeting(request):
    meet_list = ToMeet.objects.all()
    return render(request, "meeting.html", {"meet_list":meet_list})

def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list":habits_list})


def add_meet(request):
    form = request.POST
    text = form["meet_text"]
    comment = form["comment"]
    phone = form["phone"]
    tomeet = ToMeet(persone=text, comment=comment, phone_number=phone)
    tomeet.save()
    return redirect(meeting)

