from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.views.generic.edit import FormView, FormView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
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
        print(form.cleaned_data)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("users:recommend", args=[user.id]))

        return render(request, "users/login.html", context={"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm

    success_url = reverse_lazy(
        "core:home",
    )

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        pk = user.id
        print(pk)
        if user is not None:
            login(self.request, user)
            return redirect(reverse("users:recommend", args=[pk]))
        return super().form_valid(form)


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
