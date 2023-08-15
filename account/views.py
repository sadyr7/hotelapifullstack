from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import *
from account.send_email import send_confirmation_email
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, generics, status
from account.serializers import RegisterSerializer, UserSerializer, RegisterPhoneSerializer, ChangePasswordSerializer, ProfileSerializer

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

from account.utils import Util


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = CustomUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token

        # current_site = get_current_site(request).domain
        current_site = get_current_site(request).domain
        domain_without_port = current_site.split(':')[0]
        relativelink = reverse('email-verify')

        # # absurl = 'http://' + current_site + relativelink + "?token=" + str(token)
        # absurl = f'http://{domain_without_port}:3000' + relativelink + "?token=" + str(token)
        absurl = f'http://localhost:3000' + relativelink + "?token=" + str(token)

        email_body = 'hi' + user.username + 'use link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request):
        token = request.GET.get('token')
        try:
            # payload = jwt.decode(token, settings.SECRET_KEY)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')


User = get_user_model()

# class RegistrationView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         if user:
#             try:
#                 send_confirmation_email(user.email, 'http://127.0.0.1:8000/api/account/activate/?u='+str(user.activation_code))
#             except:
#                 return Response({'message': 'Зарегистрирован, но не смог отправить код активации',
#                                  'data': serializer.data}, status=201)
#
#         return Response(serializer.data, status=201)
# class RegistrationView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         send_confirmation_email(user.email, user.activation_code)
#         if user:
#             print(user, '!!!!')
#             try:
#                 send_confirmation_email(user.email,
#                                        user.activation_code)
#             except:
#                 return Response({'message':'Зарегистрировался но на почту код не отправился',
#                                 'data': serializer.data},status=201)
#         return Response(serializer.data, status=201)

# class ActivationView(GenericAPIView):
#     serializer_class = ActivationSerializer
#     permission_classes = [AllowAny,]
#
#     def post(self, request):
#         serializer = self.get_serializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response('Успешно активирован', status=200)


class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class RegistrationPhoneView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterPhoneSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('good', status=201)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('pk')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        if self.action in ['retrieve_profile', 'update_profile', 'change_password']:
            return self.request.user
        return super().get_object()

    @action(
        methods=['get'],
        detail=False,
        url_path='profile',
        serializer_class=ProfileSerializer,
        permission_classes=[IsAuthenticated]
    )
    def retrieve_profile(self, request):
        return super().retrieve(request)

    @action(
        methods=['put'],
        detail=False,
        url_path='change-password',
        serializer_class=ChangePasswordSerializer,
        permission_classes=[IsAuthenticated],
    )
    def change_password(self, request):
        return super().update(request)

    @retrieve_profile.mapping.put
    def update_profile(self, request):
        return super().update(request)

