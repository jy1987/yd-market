from django.http.response import HttpResponseNotAllowed
from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from rooms import models as room_models

# Create your views here.


def all_rooms(request):
    # print(vars(request))
    page = request.GET.get("page", default=1)
    page = int(page or 1)
    page_size = 10
    limit = page * page_size
    offset = (page - 1) * page_size
    page_count = ceil(room_models.Room.objects.count() / page_size)
    rooms = room_models.Room.objects.all()[offset:limit]
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
