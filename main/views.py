from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from requests import request
from main.models import ToDo
from. models import ToDo




def homepage(request):
    return render(request,"index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})

def second(request):
    return HttpResponse ('test 2 page')

def homework(request):
    return render(request, "meeting.html")

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)
