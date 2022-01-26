from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, Paginator
from rooms import models as room_models

# Create your views here.
class HomeView(ListView):

    model = room_models.Room
    paginate_by = 16
    ordering = "created"
    paginate_orphans = 8
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sell = "팝니다"
        context["sell"] = sell
        return context
