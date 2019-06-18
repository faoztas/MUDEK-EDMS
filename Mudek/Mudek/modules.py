# Standard Library
import random
import datetime

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# Local Django
from users.models import ActivationKey, ResetPasswordKey
from Mudek.tasks import mail_task


class ActivationKeyModule(object):

    @staticmethod
    def create_key(user, length=50):
        activation_key, created = ActivationKey.objects.get_or_create(
            user=user, is_used=False
        )

        while not activation_key.key:
            key = get_random_string(length=50)

            try:
                ActivationKey.objects.get(key=key)
            except ActivationKey.DoesNotExist:
                activation_key.key = key
                activation_key.save()

        return activation_key

    @staticmethod
    def get_key(key):
        try:
            activation_key = ActivationKey.objects.get(key=key, is_used=False)
        except ActivationKey.DoesNotExist:
            activation_key = None

        return activation_key


class ResetPasswordKeyModule(object):

    @staticmethod
    def create_key(user, length=50):
        reset_password_key, created = ResetPasswordKey.objects.get_or_create(
            user=user, is_used=False
        )

        while not reset_password_key.key:
            key = get_random_string(length=50)

            try:
                ResetPasswordKey.objects.get(key=key)
            except ResetPasswordKey.DoesNotExist:
                reset_password_key.key = key
                reset_password_key.save()

        return reset_password_key

    @staticmethod
    def get_key(key):
        try:
            reset_password_key = ResetPasswordKey.objects.get(
                key=key, is_used=False
            )
        except ResetPasswordKey.DoesNotExist:
            reset_password_key = None

        return reset_password_key


class MailModule(object):

    @staticmethod
    def send_activation_mail(activation_key):
        template_context = {
            'domain': settings.DOMAIN_BACKEND,
            'full_name': activation_key.user.get_full_name(),
            'activation_url': settings.DOMAIN_BACKEND + reverse(
                'activation', args=[activation_key.key]
            )
        }
        context = {
            'subject': _('Activate Your Account'),
            'message': _(
                "Mudek\n"
                "Hello, {full_name}\n"
                "Activate Your Account = {activation_url}\n").format(
                    full_name=template_context.get('full_name', ''),
                    activation_url=template_context.get('activation_url', '')
                ),
            'html_message': render_to_string(
                'mail/activation-mail.html', template_context
            ),
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [activation_key.user.email]
        }

        send_mail.delay(context, 'activation')

    @staticmethod
    def send_forgot_password_mail(reset_password_key):
        template_context = {
            'domain': settings.DOMAIN_BACKEND,
            'full_name': reset_password_key.user.get_full_name(),
            'reset_password_url': settings.DOMAIN_BACKEND + reverse(
                'reset-password', args=[reset_password_key.key]
            )
        }
        context = {
            'subject': _('Forgot Password'),
            'message': _(
                "Mudek\n"
                "Hello, {full_name}\n"
                "Set New Password = {reset_password_url}\n").format(
                    full_name=template_context.get('full_name', ''),
                    reset_password_url=template_context.get(
                        'reset_password_url', ''
                    )
                ),
            'html_message': render_to_string(
                'mail/forgot-password-mail.html', template_context
            ),
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [reset_password_key.user.email]
        }

        mail_task.delay(context, 'forgot-password')
