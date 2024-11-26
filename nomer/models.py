from django.db import models
from users.models import AsosiyModel, Users

class OddiyTest(AsosiyModel):
    qiymat = models.CharField(max_length=255)

    def __str__(self):
        return self.qiymat
    
class MurakkabTest(AsosiyModel):
    qiymat = models.CharField(max_length=255)

    def __str__(self):
        return self.qiymat

class Qiymat(AsosiyModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    nomer = models.CharField(max_length=255)
    link = models.CharField(max_length=255)