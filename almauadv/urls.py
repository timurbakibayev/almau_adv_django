from django.contrib import admin  # type: ignore
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.urls import path  # type: ignore
from django.conf.urls.static import static
from almauadv import settings
from app.views_cars import (
    index,
    delete,
    add_car,
)

from app.views_trips import (
    car_trips,
    car_trips_delete,
)

from app.views_login import (
    login_url,
    logout_url,
    register_url,
    forgot_password,
    forgot_password_success,
)

urlpatterns = [
    path('', index),
    path('delete/<str:id_>', delete),
    path('add_car/', add_car),
    path('cars/<int:car_id>/trips', car_trips),
    path('delete_trip/<int:trip_id>', car_trips_delete),
    path('admin/', admin.site.urls),
    path('login/', login_url),
    path('logout/', logout_url),
    path('register/', register_url),
    path('forgot_password/', forgot_password),
    path('forgot_password_success/', forgot_password_success),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
