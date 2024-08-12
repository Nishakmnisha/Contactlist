from django.db import models
from django.contrib.auth.models import User
class Contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Telephone=models.PositiveIntegerField()
    phone_number=models.PositiveIntegerField()
    def __str__(self):
        return self.email