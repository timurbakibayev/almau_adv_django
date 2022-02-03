from typing import List

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from app.car.car import Car

cars: List[Car] = [
    Car(model="Audi A6", speed=350, color="green"),
    Car(model="Toyota Corolla", speed=180, color="red"),
    Car(model="Tesla Model S", speed=390, color="gray"),
    Car(model="Honda Civic", speed=160, color="silver"),
]


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context={
        "cars": cars
    })
