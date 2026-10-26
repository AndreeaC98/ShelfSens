from django.db import models
from users.models import Users

class Items(models.Model):
    #user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    expiration_date = models.DateField()

