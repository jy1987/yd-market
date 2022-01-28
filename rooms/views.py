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
    # get data from model
    nations = room_models.Nation.objects.all()
    brands = room_models.Brand.objects.all()
    categories = room_models.Category.objects.all()
    delivery_froms = room_models.DeliveryFrom.objects.all()
    delivery_terms = room_models.DeliveryTerm.objects.all()
    colors = room_models.ItemColor.objects.all()

    # get request information from url
    name = request.GET.get("name", default="조던")
    brand = request.GET.get("brand", default="1")
    nation = request.GET.get("nation", default="1")
    category = request.GET.get("category", default="1")
    price = request.GET.get("price", 0)
    rate = request.GET.get("rate", 0)
    color = request.GET.getlist("colors")
    delivery_from = request.GET.get("delivery_from", 0)
    delivery_term = request.GET.get("delivery_term", 0)

    form_request = {
        "name": name,
        "selected_brand": int(brand),
        "selected_nation": int(nation),
        "selected_category": int(category),
        "price": int(price),
        "rate": int(rate),
        "selected_color": color,
        "selected_delivery_from": int(delivery_from),
        "selected_delivery_term": int(delivery_term),
    }
    print(form_request)
    choices_model = {
        "nations": nations,
        "brands": brands,
        "categories": categories,
        "colors": colors,
        "delivery_froms": delivery_froms,
        "delivery_terms": delivery_terms,
    }
    print(choices_model)

    # make filters and send roooms in context
    filter_kwargs = {}

    filter_kwargs["name__startswith"] = name
    filter_kwargs["nation__pk"] = nation
    filter_kwargs["brand__pk"] = brand
    filter_kwargs["categories__pk"] = category
    filter_kwargs["delivery_condition__pk"] = delivery_from
    filter_kwargs["delivery_term__pk"] = delivery_term
    # filter_kwargs["price__lte"] = price
    # filter_kwargs["color__pk__in"] = color

    rooms = room_models.Room.objects.filter(**filter_kwargs)
    print((rooms))
    return render(
        request,
        "rooms/search.html",
        context={**form_request, **choices_model, "rooms": rooms},
    )
