# для получения сигнала о создании нового объекта
from django.db.models.signals import post_save
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver

# модель в которой нужно отслеживать сигнал
from .models import Response
# для вызова функций по сигналу, которые запустят "таски"
from .views import send_mail_to_post_author, send_mail_to_response_author


@receiver(signal=post_save, sender=Response)
def notify_author_of_the_response(sender, instance, created, **kwargs):
    """
    При создании отклика, вызовется соответствующая ф-ия, которой передастся отклик.
    Когда отклик будет принят, вызовется другая ф-ия, которой так-же передастся соответствующий отклик.
    :param sender:
    :param instance: объект отклика, который сохранили в БД
    :param created: чтобы различать создание и редактирование отклика
    :param kwargs:
    :return:
    """
    if created:
        send_mail_to_post_author(instance)
    else:
        send_mail_to_response_author(instance)
