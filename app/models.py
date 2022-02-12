from django.db import models  # type: ignore


class Car(models.Model):
    model = models.CharField(max_length=1000, default="")
    speed = models.IntegerField(default=-1)
    color = models.CharField(max_length=1000, default="red")
    doors = models.IntegerField(default=4)

    def __str__(self):
        return f"{self.model}, speed: {self.speed}, {self.color}"

