import os 

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse



def home(request: HttpRequest) -> HttpResponse:
    """"""
    return render(request, 'home.html')



def hello(request: HttpRequest) -> HttpResponse:
    """"""
    return HttpResponse("Not Hello world")