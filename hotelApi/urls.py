"""
URL configuration for Full_stack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from django.conf import settings
from django.conf.urls.static import static

from account.views import UserViewSet
from hotel.views import HotelViewSet, BookingViewSet, CommentViewSet
from restourant.views import CategoryViewSet, LikeCreateView, ProductViewSet
from services_pr.views import BookingUnderServicesViewSet, SelectViewSet, ServicesViewSet

# r = routers.DefaultRouter()
# r.register('hotels', HotelViewSet)

#
r = routers.DefaultRouter()
r.register('users', UserViewSet)
r.register('booking-services', BookingUnderServicesViewSet)
r.register('bookings', BookingViewSet)
r.register('category_restourant', CategoryViewSet)
r.register('comments', CommentViewSet)
r.register('hotels', HotelViewSet)
r.register('likes', LikeCreateView)
r.register('product', ProductViewSet)
r.register('select_services', SelectViewSet)
r.register('services', ServicesViewSet)


urlpatterns = [
    path('api/account/', include(r.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
