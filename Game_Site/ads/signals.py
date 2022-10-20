# для получения сигнала о создании нового объекта
from django.db.models.signals import post_save
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver

# модель в которой нужно отслеживать сигнал
from .models import Response
from .views import send_mail_to_post_author, send_mail_to_response_author


@receiver(signal=post_save, sender=Response)
def notify_author_of_the_response(sender, instance, created, **kwargs):
    if created:
        send_mail_to_post_author(instance)
    else:
        print('response accepted')
        send_mail_to_response_author(instance)
