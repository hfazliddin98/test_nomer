from django.urls import path
from .views import nomer_yaratish

urlpatterns = [
    path('nomer_yaratish/', nomer_yaratish, name='nomer_yaratish'),
]
