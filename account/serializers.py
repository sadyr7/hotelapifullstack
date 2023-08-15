from rest_framework import serializers
from account.models import *
from account.send_sms import send_activation_sms
from django.contrib.auth import get_user_model

from django.contrib.auth.hashers import make_password, check_password

from django.contrib.auth.password_validation import validate_password

User = get_user_model()



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20,
                                     required=True, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20,
                                                  required=True, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation',
                  'first_name', 'last_name', 'username', 'avatar')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                'Пароли должны быть похожи'
            )

        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'Пароль должен содержать буквы и цифры'
                                )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    # def create(self, validated_data):
    #     return User.objects.create(
    #         email=validated_data.get('email'),
    #         first_name=validated_data.get('first_name'),
    #         last_name=validated_data.get('last_name'),
    #         phone=validated_data.get('phone_number'),
    #         address=validated_data.get('address'),
    #         password=make_password(validated_data.get('password'))
    #     )



# class ActivationSerializer(serializers.Serializer):
#     code = serializers.CharField(required=True)
#
#     def validate(self, attrs):
#         self.code = attrs['code']
#         return attrs
#
#     def save(self, **kwargs):
#         try:
#             user = User.objects.get(activation_code=self.code)
#             user.is_active = True
#             user.activation_code = ''
#             user.save()
#         except:
#             self.fail('неверный код')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('password',)


class RegisterPhoneSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=20, required=True, write_only=True, allow_null=True)
    password_confirmation = serializers.CharField(min_length=6, max_length=20, required=True,
                                                  write_only=True, allow_null=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation',
                  'first_name', 'last_name', 'username', 'phone_number')

    def validate(self, attrs):
        password = attrs['password']
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError(
                'пароли не совпадают'
            )

        if password.isdigit() or password.isalpha():
            raise serializers.ValidationError(
                'пароль должен содержать цифры и буквы'
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_sms(user.phone_number, user.activation_code)
        return user


# class ChangePasswordSerializer(serializers.Serializer):
#     model = CustomUser, UserManager
#     old_password = serializers.CharField(required=True)
#     new_password = serializers.CharField(required=True)

class ChangePasswordSerializer(UserSerializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_new_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'old_password',
            'new_password',
            'confirm_new_password',
        ]
    def validate_old_password(self, value):
        request = self.context.get('request')
        if not request.user.check_password(value):
            raise serializers.ValidationError('Old password is not correct')
        return value

    def validate_new_password(self, value):
        request = self.context.get('request')
        validate_password(value, request.user)
        return value

    def validate(self, data):
        if data.get('new_password') != data.get('confirm_new_password'):
            raise serializers.ValidationError('Password did not match')
        return data

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('new_password'))
        instance.save()
        return instance


class ProfileSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        read_only_fields = [
            'last_login',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'groups',
            'user_permissions'
        ]


class GuestReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']