from django.db import models

# Create your models here.


class Partner(models.Model):
    name = models.CharField(max_length=170, verbose_name='Название партнера')
    desc = models.TextField(max_length=400, verbose_name='Описанине партнера')
    logo = models.ImageField(upload_to='partners/logo/', verbose_name='Лого партнера')
    
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
    
    def __str__(self) -> str:
        return self.name
        
        
        
class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название клиента')
    desc = models.TextField(max_length=400, verbose_name='Описание клиента')
    photo = models.ImageField(upload_to='clients/photo', verbose_name='Фото клиента')
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        
    def __str__(self) -> str:
        return self.name