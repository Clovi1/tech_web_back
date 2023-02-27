from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile", verbose_name = 'Логин')
    phone = models.CharField(max_length = 20, blank = True, null = True, verbose_name = 'Телефон')
    image = models.ImageField(upload_to = 'images/', blank = True, null = True, verbose_name = 'Фото')
    date_creation = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Аккаунт клиента'
        verbose_name_plural = f'Аккаунты клиентов'
