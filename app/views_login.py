import random

from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse  # type: ignore
from django.shortcuts import render, redirect  # type: ignore
from django.contrib.auth.models import User  # type: ignore
from app.emails import send_email


def logout_url(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("/")


def register_url(request: HttpRequest) -> HttpResponse:
    context = {"message": "", "username": ""}
    if request.method == "POST":
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        username = request.POST.get("username", "")
        error = ""
        if username == "":
            error = "Please enter username"
        if password1 == "":
            error = "Please enter password"
        if password1 != password2:
            error = "Passwords do not match"
        if User.objects.filter(username=username).count() > 0:
            error = "User already exists. Please login."
        if error == "":
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect("/")

        context["username"] = request.POST.get("username", "")
        context["message"] = error

    return render(request, "register.html", context=context)


def login_url(request: HttpRequest) -> HttpResponse:
    context = {"message": "", "username": ""}
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username", ""),
            password=request.POST.get("password", ""),
        )
        if user is not None:
            login(request, user=user)
            return redirect("/")
        context["username"] = request.POST.get("username", "")
        context["message"] = "Incorrect login or password"

    return render(request, "login.html", context=context)


def forgot_password(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        email = request.POST.get("email", "")
        if email != "":
            try:
                user = User.objects.get(email=email)
                new_password = "".join([random.choice(list("ABCDEabcde0123456789")) for i in range(6)])
                user.set_password(new_password)
                user.save()
                text = f"Your new password is this: {new_password}"
                send_email.delay(
                    email=email,
                    text=text,
                    subject="Password Recovery",
                )
                return redirect("/forgot_password_success")
            except ObjectDoesNotExist:
                print("Some hacker tried this email", email)
                return redirect("/forgot_password_success")
    return render(request, "forgot.html")


def forgot_password_success(request: HttpRequest) -> HttpResponse:
    return render(request, "forgot_success.html")

