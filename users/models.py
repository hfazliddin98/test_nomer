from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    admin = models.BooleanField(default=False)
    talaba = models.BooleanField(default=False)
    
