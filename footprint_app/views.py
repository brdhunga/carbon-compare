import os
from typing import List

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.forms import model_to_dict

from footprint_app.models import FootPrint


def home(request: HttpRequest) -> HttpResponse:
    """"""
    user_authenticated = request.user.is_authenticated
    return render(request, 'home.html', {'is_authenticated': user_authenticated})


def hello(request: HttpRequest) -> HttpResponse:
    """"""
    return HttpResponse("Not Hello world")


def get_footprints(request: HttpRequest) -> HttpResponse:
    """"""
    full_raw_string = ""
    _template = '''       <div class="cursor-pointer w-full border-gray-100 border-b hover:bg-blue-50">
                            <div class="flex w-full items-center p-2 pl-2 border-transparent border-l-2 relative hover:border-teal-100">
                                <div class="w-6 flex flex-col items-center">
                                    <div class="flex relative w-5 h-5 bg-orange-500 justify-center items-center m-1 mr-2 w-4 h-4 mt-1 rounded-full ">
                                        <img class="rounded-full" alt="A"
                                             src="https://randomuser.me/api/portraits/thumb/men/81.jpg"></div>
                                </div>
                                <div class="w-full items-center flex">
                                    <div class="mx-2 -mt-1"><span >{}</span>
                                        <div class="text-xs truncate w-full normal-case font-normal -mt-1 text-gray-500">
                                            {}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
    '''
    footprints: List[FootPrint] = FootPrint.objects.all()

    for f in footprints:
        full_raw_string += _template.format(f.title, f.description)
    # footprints_dict = [model_to_dict(i) for i in footprints]
    return HttpResponse(full_raw_string)


def add_carbon_record(request: HttpRequest) -> HttpResponse:
    """"""
    return HttpResponse("I will add carbon footprint here.")