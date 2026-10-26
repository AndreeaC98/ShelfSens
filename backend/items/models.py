from django.db import models
from users.models import User

class Item(models.Model):
    #user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiration_date = models.DateField()

