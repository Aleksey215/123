# для получения сигнала о создании нового объекта
from django.db.models.signals import post_save
# декоратор для подключения функции к нужному сигналу
from django.dispatch import receiver
# для отправки уведомления(письма)
from django.core.mail import send_mail

# модель в которой нужно отслеживать сигнал
from .models import Response
from config.settings import DEFAULT_FROM_EMAIL


@receiver(signal=post_save, sender=Response)
def notify_author_of_the_response(sender, instance, created, **kwargs):
    # когда кто-то откликнется на объявление, его автору придет уведомление на почту
    post_author = instance.post.author
    post_title = instance.post.title
    post_author_email = instance.post.author.email
    subject = f'Dear {post_author}! You got a response on your post: {post_title}'
    response_author = instance.author
    response_content = instance.text
    message = f'Author of response: {response_author}\nContent of response: {response_content}'
    send_mail(
        subject=subject,
        message=message,
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[post_author_email]
    )
