from django.db import models
from users.models import AsosiyModel

class OddiyTest(AsosiyModel):
    qiymat = models.CharField(max_length=255)

    def __str__(self):
        return self.qiymat
    
class MurakkabTest(AsosiyModel):
    qiymat = models.CharField(max_length=255)

    def __str__(self):
        return self.qiymat
