from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def home(request):

    context = {

    }
    return render(request, 'asosiy/home.html', context)


@csrf_exempt
def kirish(request):

    context = {

    }
    return render(request, 'users/kirish.html', context)


@csrf_exempt
def chiqish(request):
    logout(request)
    return redirect('/')
