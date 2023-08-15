from django.core.mail import send_mail

def send_confirmation_email(email, code):
    print(f"Sending confirmation email to {email} with code: {code}")
    send_mail(
        'Здравствуйте, активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт, нажмите на ссылку:'
        f'\n{code}'
        f'\nНе передавайте ее никому.',
        'sadyr.top@gmail.com',
        [email],
        fail_silently=False
    )
    print("Confirmation email sent.")

# def send_confirmation_email(email, code):
#     send_mail(
#         'Здраствуйте активируйте ваш аккаунт',
#         f'Что бы активировать ваш аккаунтт скопируйте и введите на сайте код:'
#         f'\n{code}'
#         f'\n не передавайте его никому',
#         'sadyr.top@gmail.com',
#         [email],
#         fail_silently=False
#     )