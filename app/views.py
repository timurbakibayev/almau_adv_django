from typing import List
from uuid import uuid4, UUID

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from app.car.car import Car

cars: List[Car] = [
    Car(id=uuid4(), model="Audi A6", speed=350, color="green"),
    Car(id=uuid4(), model="Toyota Corolla", speed=180, color="red"),
    Car(id=uuid4(), model="Tesla Model S", speed=390, color="gray"),
    Car(id=uuid4(), model="Honda Civic", speed=160, color="silver"),
]


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html", context={
        "cars": cars
    })


def delete(request: HttpRequest, id_: str) -> HttpResponse:
    global cars
    cars = [car for car in cars if car.id != UUID(id_)]
    return HttpResponse("", status=204)


def delete_form(request: HttpRequest, id_: str) -> HttpResponse:
    global cars
    if request.method == "POST":
        cars = [car for car in cars if car.id != UUID(id_)]
        return HttpResponse("", status=204)
    return redirect("/")


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        cars.append(
            Car(
                id=uuid4(),
                model=request.POST.get("model", ""),
                speed=request.POST.get("speed", ""),
                color=request.POST.get("color", ""),
            )
        )
    return redirect("/")