from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

class RefreshToken(models.Model):
    token = models.CharField(max_length=255)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Refresh Token"

class UserProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE)
   
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
