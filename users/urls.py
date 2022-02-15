from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("<int:pk>", views.RecommendView.as_view(), name="recommend"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.SignUpView.as_view(), name="signup"),
]