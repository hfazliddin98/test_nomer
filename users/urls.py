from django.urls import path
from .views import home, kirish, chiqish

urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('chiqish/', chiqish, name='chiqish'),
]
