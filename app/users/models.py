from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_STATUS_CHOICES = (
        ('Physic', _('Физик')),
        ('Legal', _('Юрик')),
        ('Installer', _('Монтажник')),
        ('Developer', _('Застройщик'))
    )
    username = models.CharField(max_length=100, verbose_name='Юзернейм')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Почта')
    first_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=150, blank=True, null=True, verbose_name='Фамилия')
    phone = models.CharField(max_length=40, verbose_name='Телефон')
    date_joined = models.DateField(auto_now_add=True, verbose_name='Дата регистрации')
    status = models.CharField(max_length=20, choices=USER_STATUS_CHOICES, default='Physic', verbose_name='Статус')
    
    is_staff = (models.BooleanField(default=False))
    is_active = models.BooleanField(default=True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
    objects = CustomUserManager()
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        
    def __str__(self) -> str:
        return self.first_name