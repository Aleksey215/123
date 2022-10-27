# для оформления "таск"
from celery import shared_task
# для отправки писем
from django.core.mail import EmailMultiAlternatives

# адрес с которого отправятся письма
from config.settings import DEFAULT_FROM_EMAIL


@shared_task
def email_for_post_author_task(post_author, post_author_email, html_content):
    """
    "Таска" для формирования и отправки письма автору объявления об отклике на него.
    Данные берутся из функций-представлений.
    :param post_author: имя того каму отправить письмо.
    :param post_author_email: адрес куда отправить.
    :param html_content: содержание письма
    :return:
    """
    msg = EmailMultiAlternatives(
        subject=f'Hello {post_author}! You got a response on your post.',
        from_email=DEFAULT_FROM_EMAIL,
        to=[post_author_email]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def email_for_response_author_task(response_author, response_author_email, html_content):
    """
    "Таска" для формирования и отправки письма автору отклика о принятии отклика автором объявления.
    Данные берутся из функций-представлений.
    :param response_author: имя того каму отправить письмо.
    :param response_author_email: адрес куда отправить.
    :param html_content: содержание письма
    :return:
    """
    msg = EmailMultiAlternatives(
        subject=f'Hello {response_author}! Your response has been accepted.',
        from_email=DEFAULT_FROM_EMAIL,
        to=[response_author_email]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
