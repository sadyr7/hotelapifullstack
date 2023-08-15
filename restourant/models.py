from django.db import models
from account.models import CustomUser

class Category_restourant(models.Model):
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Катерогии'

class Product(models.Model):
    category = models.CharField(max_length=350)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_product = models.ImageField(upload_to='images_products/')

    
    def __str__(self):
        return f" {self.title}"

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

class Like(models.Model):
    product = models.ForeignKey(Product, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f' вы поставили лайк на {self.product}'
    
    
    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

        