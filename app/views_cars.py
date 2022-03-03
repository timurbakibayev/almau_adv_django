from django.http import HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.models import User  # type: ignore

from app.models import Car


def index(request: HttpRequest) -> HttpResponse:
    search = request.GET.get("search", "")
    cars = Car.objects.all()
    if search != "":
        if search.isnumeric():
            cars = cars.filter(model__icontains=search) | cars.filter(speed=int(search))
        else:
            cars = cars.filter(model__icontains=search)
    return render(request, "index.html", context={
        "cars": cars,
        "search": search,
    })


def delete(request: HttpRequest, id_: str) -> HttpResponse:
    Car.objects.get(id=id_).delete()
    return HttpResponse("", status=204)


def add_car(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        if request.POST.get("id_", "") == "":
            Car.objects.create(
                model=request.POST.get("model", ""),
                speed=int(request.POST.get("speed", "")),
                color=request.POST.get("color", ""),
            )
        else:
            car = Car.objects.get(pk=int(request.POST.get("id_", "")))
            car.model = request.POST.get("model", "")
            car.speed = int(request.POST.get("speed", ""))
            car.color = request.POST.get("color", "")
            car.save()
    return redirect("/")


# TODO: homework: TESTS!!!
# TODO: if a user enters non-positive (<=0) km, then message: "Only positive values allowed" FRONT-END!!
