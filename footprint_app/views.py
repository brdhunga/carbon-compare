import os 

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse



def home(request: HttpRequest) -> HttpResponse:
    """"""
    return render(request, 'home.html')


def env(request: HttpRequest) -> HttpResponse:
    return JsonResponse(dict(os.environ), safe=False)