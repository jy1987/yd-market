from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect, render
from django.http import Http404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, Paginator
from rooms import models as room_models
from rooms import forms

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


class SearchView(View):
    def get(self, request):
        form = forms.SearchForm(request.GET)

        # check if form data valid and get clean_data
        if form.is_valid():
            name = form.cleaned_data.get("name")
            nation = form.cleaned_data.get("nation")
            brand = form.cleaned_data.get("brand")
            category = form.cleaned_data.get("category")
            delivery_from = form.cleaned_data.get("delivery_from")
            delivery_term = form.cleaned_data.get("delivery_term")
            colors = form.cleaned_data.get("colors")

            filter_kwargs = {}

            if name is not None:
                filter_kwargs["name__startswith"] = name
            if nation is not None:
                filter_kwargs["nation"] = nation
            if brand is not None:
                filter_kwargs["brand"] = brand
            if category is not None:
                filter_kwargs["categories"] = category
            if delivery_from is not None:
                filter_kwargs["delivery_condition"] = delivery_from
            if delivery_term is not None:
                filter_kwargs["delivery_term"] = delivery_term
            # filter_kwargs["price__lte"] = price
            # if len(colors) > 0:
            #    filter_kwargs["color__in"] = colors

            queryset = room_models.Room.objects.filter(**filter_kwargs).order_by(
                "price"
            )

            page = request.GET.get("page", default=1)
            print(filter_kwargs)
            current_url = request.get_full_path().split("page")[0]
            if current_url[-1] == "&":
                current_url = request.get_full_path().split("page")[0][:-1]
            print(current_url)
            paginator = Paginator(queryset, 16, orphans=8)
            rooms = paginator.get_page(page)
            rooms_count = queryset.count()

            return render(
                request,
                "rooms/search.html",
                context={
                    "form": form,
                    "rooms": rooms,
                    "current_url": current_url,
                    "rooms_count": rooms_count,
                },
            )
