from unicodedata import name
from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from main.models import ToDo
from main.views import *
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

def add_meet(request):
    form2 = request.POST
    text = form2["meet_text"]
    comment = form2["comment"]
    phone = form2["phone"]
    tomeet = ToMeet(persone=text, comment=comment, phone_number=phone)
    tomeet.save()
    return redirect(meeting)


def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list":habits_list})


def add_habits(request):
    form = request.POST
    text = form["habit_text"]
    comment1 = form["comment"]
    habits = Habits(name=text, comment=comment1)
    habits.save()
    return redirect(habits)

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)




def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)