from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect, render
from django.http import Http404
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, Paginator
from rooms import models as room_models
from rooms import forms
from users import models as user_models
import pickle
import pandas as pd
import time

# Create your views here.
class HomeView(ListView):

    model = room_models.Room
    paginate_by = 16
    ordering = "created"
    paginate_orphans = 8
    context_object_name = "rooms"
    rooms_count = room_models.Room.objects.count()
    # print(rooms_count)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sell = "팝니다"
        rooms_count = self.rooms_count
        context["sell"] = sell
        context["rooms_count"] = rooms_count
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


def bigdata(a, b, c, d, e, x):
    with open(
        "/Users/jeyongkim/Dropbox/JYD/datasForAnalyzing/resultTotalBigdata_v1.cpkl",
        "rb",
    ) as f:
        clf = pickle.load(f)

    X = [a, b, c, d, e, x]
    print(X)

    sample = pd.DataFrame(
        [X],
        columns=[
            "shipping",
            "carrier",
            "day1",
            "arrival_time",
            "destination",
            "day2",
        ],
    )
    prediction_day2 = clf.predict(sample)  # 테스트용 값 산출
    print("Predicted:", len(prediction_day2))
    y = str(prediction_day2)
    print(y)
    day = y[1:-3]
    print(day)
    slot = y[-3:-1]
    print(slot)
    if slot == "25":
        hours = "0~6"
    elif slot == "50":
        hours = "6~12"
    elif slot == "75":
        hours = "12~18"
    elif a == "0" and slot == "90":
        hours = "18~24"
    elif a == "1" and slot == "90":
        hours = "16~24"
    elif slot == "30":
        hours = "0~8"
    elif slot == "60":
        hours = "8~16"
    else:
        hours = "16~24"
    interval = f"{day}일 뒤, {hours}시 사이"
    print(interval)
    return interval


class RoomDetail(DetailView):

    model = room_models.Room
    template_name = "rooms/detail.html"
    delivery_term = room_models.DeliveryTerm.objects.all()

    # context_object_name = "apple"
    def get(self, request, **kwargs):
        start = time.time()
        # get input values for bigdata
        a = request.GET.get("shipping")
        b = request.GET.get("carrier")
        c = request.GET.get("day1")
        d = request.GET.get("arrival_time")
        e = request.GET.get("destination")
        f = request.GET.get("day2")
        # get the count from request for calculating total price
        count = request.GET.get("count", 1)

        if (
            a is not None
            and b is not None
            and c is not None
            and d is not None
            and e is not None
            and f is not None
        ):
            result = bigdata(a, b, c, d, e, f)
        else:
            result = "배송예측결과"
        self.object = self.get_object()
        # get objects of room's host rooms
        room = self.object
        host_rooms = room.host.rooms.all()[:4]

        context = super().get_context_data(**kwargs)
        delivery_term = self.delivery_term
        context["delivery_term"] = delivery_term
        context["result"] = result
        context["host_rooms"] = host_rooms
        end = time.time()
        time_interval = end - start
        context["interval"] = time_interval
        context["count"] = count
        total_price = int(count) * room.price

        context["sum"] = total_price

        return self.render_to_response(context)


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
            # print(filter_kwargs)
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


class BuyView(SearchView):
    def get(self, request):
        form = forms.SearchForm(request.GET)
        superhost = user_models.User.objects.filter(superhost=True)
        # host = room_models.Room.objects.filter(superhost == True)
        superhosts = []
        for s in superhost.all():
            superhosts.append(s.username)
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
            filter_kwargs["host__username__in"] = superhosts
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
            print(queryset.count())

            page = request.GET.get("page", default=1)
            # print(filter_kwargs)
            current_url = request.get_full_path().split("page")[0]
            if current_url[-1] == "&":
                current_url = request.get_full_path().split("page")[0][:-1]
            print(current_url)
            paginator = Paginator(queryset, 16, orphans=8)
            rooms = paginator.get_page(page)
            rooms_count = queryset.count()

            return render(
                request,
                "rooms/buy.html",
                context={
                    "form": form,
                    "rooms": rooms,
                    "current_url": current_url,
                    "rooms_count": rooms_count,
                },
            )


class SellView(View):
    def get(self, request):
        form = forms.SearchForm(request.GET)
        superhost = user_models.User.objects.filter(superhost=False)
        # host = room_models.Room.objects.filter(superhost == True)
        superhosts = []
        for s in superhost.all():
            superhosts.append(s.username)
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
            filter_kwargs["host__username__in"] = superhosts
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
            print(queryset.count())

            page = request.GET.get("page", default=1)
            # print(filter_kwargs)
            current_url = request.get_full_path().split("page")[0]
            if current_url[-1] == "&":
                current_url = request.get_full_path().split("page")[0][:-1]
            print(current_url)
            paginator = Paginator(queryset, 16, orphans=8)
            rooms = paginator.get_page(page)
            rooms_count = queryset.count()

            return render(
                request,
                "rooms/sell.html",
                context={
                    "form": form,
                    "rooms": rooms,
                    "current_url": current_url,
                    "rooms_count": rooms_count,
                },
            )
