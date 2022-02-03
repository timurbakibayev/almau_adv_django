from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from app.views import (
    index,
    delete,
    delete_form,
    add_car,
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('delete_form/<str:id_>', delete_form),
    path('add_car/', add_car),
    path('admin/', admin.site.urls),
]
