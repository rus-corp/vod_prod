from django.db import models
from django.utils.text import slugify
from transliterate import translit

class MainCategory(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True)
    
    class Meta:
        verbose_name = 'Главная категория'
        verbose_name_plural = 'Главные категории'
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        try:
            name = translit(self.name, reversed=True)
            self.slug = slugify(name)
        except:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE, related_name='categories', verbose_name='Главная категория')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    def __str__(self) -> str:
        return self.name
        
    def save(self, *args, **kwargs):
        try:
            name = translit(self.name, reversed=True)
            self.slug = slugify(name)
            
        except:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
        
        
        
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    power = models.FloatField(verbose_name='Мощность', null=True, blank=True)
    desc = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена', null=True, blank=True)
    photo = models.ImageField(upload_to='product/images', verbose_name='Фото', null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Готов к продаже')
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
    def __str__(self) -> str:
        return self.name
 
    def save(self, *args, **kwargs):
        try:
            name = translit(self.name, reversed=True)
            self.slug = slugify(name)
        except:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    
    
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stocks', verbose_name='Продукт')
    count = models.IntegerField(default=1, verbose_name='Количество')
    
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        
    def __str__(self) -> str:
        return f'{self.product.name} - {self.count}'
    
    def save(self, *args, **kwargs):
        if self.count == 0:
            self.product.is_published = False
        else:
            self.product.is_published = True
        return super().save(*args, **kwargs)
