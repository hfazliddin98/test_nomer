from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Users



@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'admin', 'talaba', 'parol']



admin.site.unregister(Group)