from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import RegisterView, LoginView, UserListView, RegistrationPhoneView, VerifyEmail, UserViewSet
from hotel.views import BookingViewSet, HotelViewSet, CommentViewSet
from restourant.views import ProductViewSet, CategoryViewSet, LikeCreateView
from services_pr.views import ServicesViewSet, SelectViewSet, BookingUnderServicesViewSet

# router = routers.DefaultRouter()
# router.register('', UserViewSet)
# router.register('booking-services', BookingUnderServicesViewSet)
# router.register('bookings', BookingViewSet)
# router.register('category_restourant', CategoryViewSet)
# router.register('comments', CommentViewSet)
# router.register('hotels', HotelViewSet)
# router.register('likes', LikeCreateView)
# router.register('product', ProductViewSet)
# router.register('select_services', SelectViewSet)
# router.register('services', ServicesViewSet)

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('register-phone/', RegistrationPhoneView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('bookings/', UserListView.as_view()),
    # path('', include(router.urls)),
]






