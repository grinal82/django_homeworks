from django.http import HttpResponse
from django.shortcuts import render, reverse
import time
import os


def home_view(request):
    template_name = "app/home.html"
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        "Главная страница": reverse("home"),
        "Показать текущее время": reverse("time"),
        "Показать содержимое рабочей директории": reverse("workdir"),
    }

    context = {"pages": pages}
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = time.asctime()
    msg = f"Текущее время: {current_time}"
    return HttpResponse(msg)


def workdir_view(request):
    rez = sorted(os.listdir(path=(".")))
    print(rez)
    for n, item in enumerate(rez):
        print(n + 1, item)
    result = ", ".join(rez)
    return HttpResponse(result)
