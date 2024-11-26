from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, IshtirokchiForm
from .models import Users
from nomer.models import Qiymat



@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        userlar = Users.objects.filter(talaba=True)
        user_name = f'{request.user.last_name} {request.user.first_name}'
        qiymat = Qiymat.objects.filter(user = Users.objects.get(id=request.user.id))

        context = {
            'qiymat':qiymat,
            'user_name':user_name,
            'userlar':userlar,
        }
        return render(request, 'asosiy/home.html', context)

    else:
        return redirect('kirish')    


@csrf_exempt
def kirish(request):
    if request.user.is_authenticated:
        return redirect('/')    
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                    return redirect('/')
                else:        
                    return HttpResponse('<center><h1>JSHR yoki parol xato !!!</h1></center>')
            else:
                return redirect('kirish')
            
        else:
            form = LoginForm()

            context = {
                'form':form,
            }
            return render(request, 'users/kirish.html', context)


@csrf_exempt
def chiqish(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def royhat(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IshtirokchiForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.admin = False
                user.talaba = True
                user.parol = user.password
                user.password = make_password(user.password)
                user.save()
                return redirect('/')
        else:
            form = IshtirokchiForm()

            context = {
                'form':form,
            }
            return render(request, 'users/ishtirokchi_qoshish.html', context)

    else:
        return render(request, 'asosiy/404.html')