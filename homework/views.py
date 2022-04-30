from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def homework(request):
    return render(request, "homework.html")

def homework2 (request):
    return HttpResponse("Добро пожаловать в приложение ToDo - Admin")
