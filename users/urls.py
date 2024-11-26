from django.urls import path
from .views import home, kirish, chiqish, royhat

urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('chiqish/', chiqish, name='chiqish'),
    path('royhat/', royhat, name='royhat'),
]
