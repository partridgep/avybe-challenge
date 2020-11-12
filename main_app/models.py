from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length= 100)

    def __str__(self):
        return f'{self.nickname}'

    def get_absolute_url(self):
        return reverse('home')

class Picture(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Picture for {self.user_id} @{self.url}'
