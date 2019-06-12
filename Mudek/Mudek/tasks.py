# Django
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

# Local Django
# from Mudek import celery_app
# # from tasks.models import Reminder


# @celery_app.task
# def mail_task(context, verb):
#     """
#     Context Format
#         context = {
#             subject="subject"
#             message="messages"
#             html_message=render_to_string('email/email.html', template_context),
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=[email]
#         }
#     """

#     try:
#         send_mail(**context)

#         return ','.join(context['recipient_list']) + ' success = ' + verb
#     except:
#         return ','.join(context['recipient_list']) + ' error = ' + verb


# @celery_app.task
# def reminder_mail_task(reminder_id, verb):
#     try:
#         reminder = Reminder.objects.get(id=reminder_id)
#     except Reminder.DoesNotExist:
#         return 'Reminder - {reminder_id} not found = {verb}'.format(
#             reminder_id=reminder_id, verb=verb
#         )

#     template_context = {
#         'domain': settings.DOMAIN_BACKEND,
#         'full_name': reminder.task.user.get_full_name(),
#         'title': reminder.task.title,
#         'description': reminder.task.description
#     }
#     context = {
#         'subject': _('Reminder'),
#         'message': _(
#             "Mudek\n"
#             "Hello, {full_name}\n"
#             "It's time for the task.\n"
#             "'{title}'\n"
#             "{description}").format(
#                 full_name=template_context.get('full_name', ''),
#                 title=template_context.get('title', ''),
#                 description=template_context.get('description', '')
#             ),
#         'html_message': render_to_string(
#             'mail/reminder-mail.html', template_context
#         ),
#         'from_email': settings.DEFAULT_FROM_EMAIL,
#         'recipient_list': [reminder.task.user.email]
#     }

#     try:
#         send_mail(**context)

#         return ','.join(context['recipient_list']) + ' success = ' + verb
#     except:
#         return ','.join(context['recipient_list']) + ' error = ' + verb
