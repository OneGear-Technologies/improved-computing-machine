import random
import string
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def generate_unique_code():
    length=6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Wallet.objects.filter(wid=code).count() == 0:
            break

    return code

class Wallet(models.Model):
    uid = models.IntegerField(default=0)
    first_name = models.CharField(max_length=800, default="")
    last_name = models.CharField(max_length=800, default="")
    wid = models.CharField(max_length=8,default=generate_unique_code ,unique=True)
    amount= models.IntegerField(default=0)

    def __str__(self):
        return str(self.wid)