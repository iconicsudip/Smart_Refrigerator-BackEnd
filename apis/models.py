from djongo import models
from django.contrib.auth.models import User
# Create your models here.
class ValidUser(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    def __str__(self):
        return str(self.username)
