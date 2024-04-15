from django.shortcuts import render, HttpResponse
from django.urls import reverse
import request


# Create your views here.
def index(request):
    nid = request.GET.get('nid')
    print(nid)
    return HttpResponse("index")


def login(request):
    return HttpResponse("login")
