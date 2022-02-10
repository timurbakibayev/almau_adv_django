from typing import List, Optional

from django.http import HttpResponseRedirect
from django.test import TestCase, Client  # type: ignore


def cars_number(cars: List, model: str, speed: int, color: str) -> int:
    quantity = 0
    for car in cars:
        if car.model == model and car.speed == speed and car.color == color:
            quantity += 1
    return quantity


def car_id(cars: List, model: str, speed: int, color: str) -> Optional[int]:
    for car in cars:
        if car.model == model and car.speed == speed and car.color == color:
            return car.id
    return None


class TestCars(TestCase):
    def setUp(self):
        ...

    def test_add_car(self):
        c = Client()
        response = c.get("/")
        assert "cars" in response.context
        number_of_cars = len(response.context["cars"])
        response = c.post("/add_car/", {
            "model": "Porsche",
            "speed": 340,
            "color": "red",
        })
        assert isinstance(response, HttpResponseRedirect)
        assert response.url == "/"
        response = c.get("/")
        assert "cars" in response.context
        self.assertEquals(len(response.context["cars"]), number_of_cars + 1)
        assert 'button onclick="delete_car' in response.content.decode("UTF8")
        assert cars_number(
            cars=response.context["cars"],
            model="Porsche",
            speed=340,
            color="red",
        ) == 1

    def test_delete_car(self):
        c = Client()
        c.post("/add_car/", {
            "model": "Jeep",
            "speed": 200,
            "color": "green",
        })
        response = c.get("/")
        assert "cars" in response.context
        number_of_cars = len(response.context["cars"])
        assert cars_number(
            cars=response.context["cars"],
            model="Jeep",
            speed=200,
            color="green",
        ) == 1

        id_ = car_id(
            cars=response.context["cars"],
            model="Jeep",
            speed=200,
            color="green",
        )
        c.get(f"/delete/{id_}")

        response = c.get("/")
        self.assertEquals(len(response.context["cars"]), number_of_cars-1)
        assert cars_number(
            cars=response.context["cars"],
            model="Jeep",
            speed=200,
            color="green",
        ) == 0
