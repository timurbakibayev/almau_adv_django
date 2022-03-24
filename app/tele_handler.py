from typing import Dict

from django.contrib.auth.models import User
from app.telefunctions import send_message
from app.models import Car

context: Dict[User, str] = dict()
inputs: Dict[User, Dict[str, str]] = dict()


def handle_message(user: User, text: str):
    global context, inputs
    if user not in context:
        context[user] = ""
        inputs[user] = dict()

    if text == "/list":
        for car in Car.objects.filter(user=user):
            send_message(user, f"{car}, edit: /edit_{car.id}")
        return

    if text[:6] == "/edit_":
        car = Car.objects.get(pk=int(text.split("_")[1]))
        send_message(user, f"Going to edit this car: {car}")
        context[user] = "edit_car"
        inputs[user]["id"] = str(car.id)

    if text == "/add":
        context[user] = "add_car"
    if context[user] == "add_car":
        context[user] = "add_car_model"
        send_message(user, f"Please enter model")
        return
    if context[user] == "edit_car":
        context[user] = "edit_car_model"
        send_message(user, f"Please enter model")
        return
    if context[user] == "add_car_model":
        inputs[user]["model"] = text
        context[user] = "add_car_speed"
        send_message(user, f"Please enter speed")
        return
    if context[user] == "edit_car_model":
        inputs[user]["model"] = text
        context[user] = "edit_car_speed"
        send_message(user, f"Please enter speed")
        return
    if context[user] == "add_car_speed":
        inputs[user]["speed"] = text
        context[user] = "add_car_color"
        send_message(user, f"Please enter color")
        return
    if context[user] == "edit_car_speed":
        inputs[user]["speed"] = text
        context[user] = "edit_car_color"
        send_message(user, f"Please enter color")
        return
    if context[user] == "add_car_color":
        inputs[user]["color"] = text
        context[user] = ""
        car = Car.objects.create(
            user=user,
            model=inputs[user]["model"],
            speed=int(inputs[user]["speed"]),
            color=inputs[user]["color"],
        )
        send_message(user, f"Car added: {car}")
        return
    if context[user] == "edit_car_color":
        inputs[user]["color"] = text
        context[user] = ""
        car = Car.objects.get(pk=int(inputs[user]["id"]))
        car.model = inputs[user]["model"]
        car.speed = inputs[user]["speed"]
        car.color = inputs[user]["color"]
        car.save()
        send_message(user, f"Car edited: {car}")
        return

    send_message(user, f"Please type a proper command: /list , /add or /edit")

