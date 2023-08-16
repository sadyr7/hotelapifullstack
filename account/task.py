from django.core.mail import send_mail
from hotelApi.celery import app
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from datetime import datetime
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@app.task(bind=True)
def send_activation_email(self, email, code):
    send_mail(
        subject='Код Активации',
        message=f'Press in order to activate your account\n'
        f'http://localhost:3000/api/account/activate/?c={code}\n',
        from_email='sadyr.top@gmail.com',
        recipient_list=[email],
        fail_silently=True)
    return 'Done'


@app.task(bind=True)
def send_confirmation_password_task(self, email, code):
    send_mail(
        subject='Здравствуйте, подтвердите новый пароль',
        message=f'http://localhost:3000/api/reset-password/confirm/?c={code}',
        from_email='sadyr.top@gmail.com',
        recipient_list=[email],
        fail_silently=False)


@app.task(bind=True)
def clear_tokens(self):
    BlacklistedToken.objects.filter(token__expires_at__lt=datetime.now()).delete()
    OutstandingToken.objects.filter(expires_at__lt=datetime.now()).delete()
    return 'Deleted expired tokens'