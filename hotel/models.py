from django.db import models
from account.models import CustomUser


# Create your models here.

class AbstractNameDescription(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    objects = models.Manager()

    class Meta:
        abstract = True

class Hotel(AbstractNameDescription):

    category = models.CharField(max_length=250)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)
    image4 = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отель'


class Booking(models.Model):
    room = models.CharField(max_length=500)
    guest = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='bookings')
    time = models.TimeField()
    date = models.DateField()


    objects = models.Manager()

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронировании'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented: {self.body}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'