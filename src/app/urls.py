# 3rd party
from django.urls import path

from . import views

urlpatterns = [
    path("cars/", views.CarDetails.as_view()),
    path("cars/<int:pk>/", views.DeleteCar.as_view()),
    path("rate/", views.AddRate.as_view()),
    path("popular/", views.PopularCars.as_view()),
]
