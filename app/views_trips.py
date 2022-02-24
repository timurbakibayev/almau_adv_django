from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from app.models import (
    Car,
    Trip,
)


def car_trips(request: HttpRequest, car_id: int) -> HttpResponse:
    if request.method == "POST":
        if request.POST.get("id_", "") == "":
            Trip.objects.create(
                car_id=car_id,
                km=int(request.POST.get("trip_km", "")),
                date=request.POST.get("trip_date", ""),
            )
        else:
            trip = Trip.objects.get(pk=int(request.POST.get("id_", "")))
            trip.km = int(request.POST.get("trip_km", ""))
            trip.date = date=request.POST.get("trip_date", "")
        return redirect(f"/cars/{car_id}/trips")

    context = dict()
    car = Car.objects.get(id=car_id)
    context["car"] = car
    context["trips"] = Trip.objects.filter(car=car)

    return render(request, "trips.html", context=context)


def car_trips_delete(request: HttpRequest, trip_id: int) -> HttpResponse:
    if request.method == "DELETE":
        Trip.objects.get(id=trip_id).delete()
        return HttpResponse("", status=204)

    return HttpResponse("Method not allowed (only DELETE)", status=405)


# TODO: class: pagination for trips
# TODO: class: filtering for trips by date

# TODO: homework: TESTS!!!
