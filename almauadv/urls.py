from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from app.views import (
    index,
    delete,
    add_car,
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('add_car/', add_car),
    path('admin777/', admin.site.urls),
]
