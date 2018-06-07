from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class task(models.Model):
	name = models.CharField(max_length = 250)
	desc = models.CharField(max_length = 500)
	status = models.BooleanField(default = False)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

