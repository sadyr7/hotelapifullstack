from django.db import models


# Create your models here.


class Services(models.Model):
    service = models.CharField(max_length=250)

    img = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()

    def __str__(self):
        return self.service


class SelectCategory(models.Model):
    select_category = models.CharField(max_length=500)

    def __str__(self):
        return self.select_category


class Booking_s(models.Model):
    service = models.CharField(max_length=350)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()










