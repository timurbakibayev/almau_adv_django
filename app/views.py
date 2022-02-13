from django.http import HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.models import User  # type: ignore

from app.models import Car

car_id_to_edit = ''


def index(request: HttpRequest) -> HttpResponse:
    catalog = Car.objects.all()
    return render(request, "index.html", context={
        "cars": catalog
    })


def delete(request: HttpRequest, id_: str) -> HttpResponse:
    global cars
    Car.objects.get(id=id_).delete()
    return HttpResponse("", status=204)

def set_car_to_edit(request: HttpRequest, id_: str) -> HttpResponse: 
    car_id_to_edit = id_
    # if request.method == "POST":
    #     car = Car.objects.get(id=id_)
    #     car.model = request.POST.get("model", "")
    #     car.speed = int(request.POST.get("speed", ""))
    #     car.color = request.POST.get("color", "")
    #     car.save()
    return HttpResponse("", status=204)

def edit_car(request: HttpRequest, id_: str) -> HttpResponse:
    if request.method == "POST":
        car = Car.objects.get(id=id_)
        car.model = request.POST.get("model", "")
        car.speed = int(request.POST.get("speed", ""))
        car.color = request.POST.get("color", "")
        car.save()
    return redirect('/')
def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        Car.objects.create(
            model=request.POST.get("model", ""),
            speed=int(request.POST.get("speed", "")),
            color=request.POST.get("color", ""),
        )
    return redirect("/")
