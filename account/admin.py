from django.contrib import admin

from account.models import CustomUser
from hotel.models import Hotel, Booking, Comment

admin.site.register(CustomUser)
admin.site.register(Hotel)

admin.site.register(Booking)
admin.site.register(Comment)