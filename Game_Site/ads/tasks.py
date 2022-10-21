from celery import shared_task
from django.core.mail import EmailMultiAlternatives

from config.settings import DEFAULT_FROM_EMAIL


@shared_task
def email_for_post_author_task(post_author, post_author_email, html_content):
    print('send response')
    msg = EmailMultiAlternatives(
        subject=f'Hello {post_author}! You got a response on your post.',
        from_email=DEFAULT_FROM_EMAIL,
        to=[post_author_email]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def email_for_response_author_task(response_author, response_author_email, html_content):
    print('response accept')
    msg = EmailMultiAlternatives(
        subject=f'Hello {response_author}! Your response has been accepted.',
        from_email=DEFAULT_FROM_EMAIL,
        to=[response_author_email]
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
