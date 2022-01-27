from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.http import Http404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
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


"""
def room_detail(request, pk):
    try:
        room = room_models.Room.objects.get(pk=pk)
        # print(dir(room))
        return render(request, "rooms/room_detail.html", context={"room": room})
    except ObjectDoesNotExist:
        return redirect(reverse("core:home"))
        # raise Http404()
"""


class RoomDetail(DetailView):

    model = room_models.Room
    template_name = "rooms/detail.html"
    # context_object_name = "apple"


def search(request):
    name = request.GET.get("name", default="조던")
    nations = room_models.Nation.objects.all()
    brands = room_models.Brand.objects.all()
    categories = room_models.Category.objects.all()
    delivery_from = room_models.DeliveryFrom.objects.all()
    delivery_term = room_models.DeliveryTerm.objects.all()
    colors = room_models.ItemColor.objects.all()

    brand = request.GET.get("brand", default="1")
    nation = request.GET.get("nation", default="1")
    category = request.GET.get("category", default="1")
    price = request.GET.get("price", 0)
    rate = request.GET.get("rate", 0)
    color = request.GET.getlist("colors")
    print(color)
    form_request = {
        "name": name,
        "selected_brand": int(brand),
        "selected_nation": int(nation),
        "selected_category": int(category),
        "price": int(price),
        "rate": int(rate),
        "selected_color": color,
    }
    print(form_request)
    choices_model = {
        "nations": nations,
        "brands": brands,
        "categories": categories,
        "colors": colors,
    }
    print(choices_model)
    return render(
        request,
        "rooms/search.html",
        context={**form_request, **choices_model},
    )
