from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from app.views import (
    index,
)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]
