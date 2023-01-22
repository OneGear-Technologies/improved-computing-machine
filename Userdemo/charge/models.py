from django.db import models

# Create your models here.

class StatProfile(models.Model):
    #user = models.ForeignKey('auth.User',on_delete = models.SET_NULL,null=True,blank=True)

    cid = models.IntegerField(unique=True)
    charge_stat = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.cid)
