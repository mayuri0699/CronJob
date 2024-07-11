from django.db import models

# Create your models here.

class UserNumber(models.Model):
    usernumber = models.IntegerField(null=True, blank=True)