from django.http import HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.models import User  # type: ignore

from app.models import Car
from app.telefunctions import send_message


def index(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect("/login")
    search = request.GET.get("search", "")
    cars = Car.objects.filter(user=request.user)
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
    if request.user.is_anonymous:
        return redirect("/login")
    send_message(request.user, f"You are deleting this car: {Car.objects.get(id=id_)}")
    Car.objects.get(id=id_).delete()
    return HttpResponse("", status=204)


def add_car(request: HttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        if request.POST.get("id_", "") == "":
            car = Car.objects.create(
                user=request.user,
                model=request.POST.get("model", ""),
                speed=int(request.POST.get("speed", "")),
                color=request.POST.get("color", ""),
            )
            send_message(request.user, f"You have added this car: {car}")
        else:
            car = Car.objects.get(pk=int(request.POST.get("id_", "")))
            send_message(request.user, f"You are updating this car: {car}")
            if car.user != request.user:
                return redirect("/")
            car.model = request.POST.get("model", "")
            car.speed = int(request.POST.get("speed", ""))
            car.color = request.POST.get("color", "")
            car.save()
            send_message(request.user, f"It is now like this: {car}")
    return redirect("/")


# TODO: homework: TESTS!!!
# TODO: if a user enters non-positive (<=0) km, then message: "Only positive values allowed" FRONT-END!!
