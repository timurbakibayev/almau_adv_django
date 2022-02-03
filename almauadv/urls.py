from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from app.views import (
    plus_view,
    minus_view,
    index,
)

urlpatterns = [
    path('', index),
    path('plus/<int:a>/<int:b>/', plus_view),
    path('minus/<int:a>/<int:b>/', minus_view),
    path('admin/', admin.site.urls),
]
