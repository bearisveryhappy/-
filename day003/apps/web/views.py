from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def info (request):

    return HttpResponse("info")


def login (request):
    return HttpResponse("login")