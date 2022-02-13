from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from app.views import (
    set_car_to_edit,
    edit_car,
    index,
    delete,
    add_car,
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('set_car_to_edit/<str:id_>', set_car_to_edit),
    path('edit_car/<str:id_>', edit_car),
    path('add_car/', add_car),
    path('admin777/', admin.site.urls),
]
