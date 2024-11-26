import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from users.models import Users
from .models import OddiyTest, MurakkabTest, Qiymat


def get_random_two_numbers():
    # Barcha qiymatlarni olamiz
    all_nomers = list(OddiyTest.objects.all())
    if len(all_nomers) < 2:
        return HttpResponse("Yetarli qiymatlar mavjud emas!")  # Kamida 2 ta qiymat kerak
    return random.sample(all_nomers, 2)


def get_random_one_numbers():
    # Barcha qiymatlarni olamiz
    all_nomers = list(MurakkabTest.objects.all())
    if len(all_nomers) < 1:
        return HttpResponse("Yetarli qiymatlar mavjud emas!")  # Kamida 1 ta qiymat kerak
    return random.sample(all_nomers, 1)


@csrf_exempt
def nomer_yaratish(request):
    qiymat = Qiymat.objects.filter(user=Users.objects.get(id=request.user.id))
    if qiymat:

        return redirect('/')
    else:
        for d in get_random_two_numbers():
            Qiymat.objects.create(
                user = Users.objects.get(id=request.user.id),
                nomer = d.qiymat,
                link = f'https://robocontest.uz/tasks/{d.qiymat}'
            )

        for d in get_random_one_numbers():
            Qiymat.objects.create(
                user = Users.objects.get(id=request.user.id),
                nomer = d.qiymat,
                link = f'https://robocontest.uz/tasks/{d.qiymat}'
            )

        return redirect('/')




