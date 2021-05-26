from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse(get_file())


def get_file():
    with open('lesson3.json', 'r', encoding='utf-8') as file:
        return file.read()
