from django.shortcuts import render
from django.views.generic import View, DetailView
from users import models as user_models
from rooms import models as room_models
from users import forms

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", context={"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            print(email, password)

        return render(request, "users/login.html", context={"form": form})


class RecommendView(DetailView):
    model = user_models.User
    template_name = "users/recommend.html"

    def get(self, request, **kwargs):

        self.object = self.get_object()
        user = self.object

        brand_id = user.brand_id
        nation_id = user.nation_id
        category_id = user.categories_id

        filter_kwargs = {}

        if nation_id is not None:
            filter_kwargs["nation"] = nation_id
        if brand_id is not None:
            filter_kwargs["brand"] = brand_id
        if category_id is not None:
            filter_kwargs["categories"] = category_id

        rooms = room_models.Room.objects.filter(**filter_kwargs).order_by("price")
        brand = room_models.Brand.objects.filter(id=brand_id)
        nation = room_models.Nation.objects.filter(id=nation_id)
        category = room_models.Category.objects.filter(id=category_id)

        # print(brand_id, nation_id, category_id)
        # print(rooms)
        context = self.get_context_data(object=self.object)
        context["rooms"] = rooms
        context["brand"] = brand
        context["nation"] = nation
        context["category"] = category
        return self.render_to_response(context)
