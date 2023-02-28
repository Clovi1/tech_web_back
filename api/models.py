from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile", verbose_name = 'Логин')
    phone = models.CharField('Телефон', max_length = 20, blank = True, null = True)
    image = models.ImageField('Фото', upload_to = 'images/', blank = True, null = True)
    date_create = models.DateTimeField('Время создания', auto_now_add = True)
    date_update = models.DateTimeField('Время обновления', auto_now = True)

    class Meta:
        verbose_name = 'Аккаунт клиента'
        verbose_name_plural = f'Аккаунты клиентов'


class Tags(models.Model):
    name = models.CharField('Название', max_length = 100, db_index = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = f'Теги'


class Posts(models.Model):
    title = models.CharField('Заголовок', max_length = 255)
    content = models.TextField('Текст статьи')
    image = models.ImageField('Фото', upload_to = 'images/', blank = True, null = True)
    tags = models.ManyToManyField(Tags, verbose_name = 'Категория')
    author = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.CASCADE)
    views_count = models.IntegerField(default = 0)
    date_create = models.DateTimeField('Время создания', auto_now_add = True)
    date_update = models.DateTimeField('Время обновления', auto_now = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = f'Посты'
