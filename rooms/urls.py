from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="detail"),
    # path("<int:pk>/predict/", views.predict, name="predict"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("buy/", views.BuyView.as_view(), name="buy"),
    path("sell/", views.SellView.as_view(), name="sell"),
]
