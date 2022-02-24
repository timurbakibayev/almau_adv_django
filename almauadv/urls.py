from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from app.views_cars import (
    index,
    delete,
    add_car,
)

from app.views_trips import (
    car_trips,
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('add_car/', add_car),
    path('cars/<int:id_>', car_trips),
    path('admin/', admin.site.urls),
]
