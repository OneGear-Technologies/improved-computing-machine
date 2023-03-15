from django.db import models
from random import randint
import datetime

# Create your models here.

def generate_code():
    n=3
    while True:
        code='OGT-'+''.join(["{}".format(randint(0, 9)) for num in range(0, n)])
        if StatProfile.objects.filter(cid=code).count() == 0:
            break
    return code

class StatProfile(models.Model):
    #user = models.ForeignKey('auth.User',on_delete = models.SET_NULL,null=True,blank=True)

    cid = models.CharField(max_length=8, default=generate_code, unique=True)
    uid = models.IntegerField(default=0)
    charge_stat = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    op = models.CharField(max_length=100, default='')
    loc = models.CharField(max_length=100, default='')

    def __str__(self) -> str:
        return str(self.cid)
