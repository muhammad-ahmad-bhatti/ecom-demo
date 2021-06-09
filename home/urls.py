from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home.as_view(),  name="home"),
    path("details<int:pk>", views.Details.as_view(), name="details")
]
