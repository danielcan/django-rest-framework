from celery import shared_tasks
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django_celery import settings

@shared_tasks
def send_emails_users():
    asunto = 'Mensaje de prueba'
    mensaje = 'Bienvenido, esto es un mensaje de prueba CELERY, RABBITMQ Y DJANGO'
    users = User.objects.get(username="daniel")
    for user in users:
        send_mail(asunto, mensaje, settings.Email_HOST_USER,
                  [user.email], fail_silently=False)
        return '{} se envio el correo correctamente'.format(user)