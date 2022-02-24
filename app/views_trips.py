from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from app.models import (
    Car,
    Trip,
)


def car_trips(request: HttpRequest, id_: int) -> HttpResponse:
    context = dict()
    car = Car.objects.get(id=id_)
    context["car"] = car
    context["trips"] = Trip.objects.filter(car=car)

    return render(request, "trips.html", context=context)


# TODO: homework: Implement trips CRUD
# TODO: class: pagination for trips
# TODO: class: filtering for trips by date

# TODO: homework: TESTS!!!
