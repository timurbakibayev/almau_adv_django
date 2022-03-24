from django.contrib.auth.models import User
from django.db import models  # type: ignore


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=1000, default="")
    speed = models.IntegerField(default=-1)
    color = models.CharField(max_length=1000, default="red")
    doors = models.IntegerField(default=4)

    def __str__(self):
        return f"{self.model}, speed: {self.speed}, {self.color}"

    def total_trip_km(self) -> int:
        return sum(
            trip.km
            for trip in Trip.objects.filter(car=self)
        )


class Trip(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    km = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.car}: {self.date}, {self.km} km"


class Teleuser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    chat_id = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.chat_id}"
