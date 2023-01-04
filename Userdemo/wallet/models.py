from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Wallet(models.Model):
	uid = models.ForeignKey(User, on_delete=models.CASCADE)
	wid = models.IntegerField()
	amount= models.IntegerField()
	def __str__(self):
		return str(self.wid)
