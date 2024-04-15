from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
def anth (request):

    return  HttpResponse("fksldfjhaksd1")
    # return render(request,'api/anth.html')


def login (request):
    # url = reverse('v2',args=(2223,'1231231'))
    # print(url)
    print(request.path_info)
    print(request.GET)
    print(request.GET.get("age"))
    print(request.method)
    print(request.resolver_match)
    return HttpResponse("login")