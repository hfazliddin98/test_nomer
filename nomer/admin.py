from django.contrib import admin
from .models import OddiyTest, MurakkabTest, Qiymat


@admin.register(OddiyTest)
class OddiyTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'qiymat']
    search_fields = ['id', 'qiymat']


@admin.register(MurakkabTest)
class MurakkabTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'qiymat']
    search_fields = ['id', 'qiymat']


@admin.register(Qiymat)
class QiymatAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'nomer', 'link']
    search_fields = ['id', 'user', 'nomer', 'link']