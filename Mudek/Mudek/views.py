# Django
from django.conf import settings
from django.contrib import messages
from django.views.static import serve
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _

# Local Django
from users.models import ActivationKey
from Mudek.forms import ResetPasswordForm
from Mudek.variables import RESET_PASSWORD_FORM_PREFIX
from Mudek.modules import ActivationKeyModule, ResetPasswordKeyModule


class ActivationView(TemplateView):
    template_name = 'activation.html'

    def dispatch(self, request, key, *args, **kwargs):
        self.activation(key)

        if request.user.is_authenticated():
            if self.activation_key:
                messages.success(request, self.activation_message)
            else:
                messages.error(request, self.activation_message)

            return redirect('/admin/')

        return super(ActivationView, self).dispatch(
            request, key, *args, **kwargs
        )

    def get_context_data(self, **kwargs):
        context = super(ActivationView, self).get_context_data(**kwargs)

        context.update({
            'title': 'Activation',
            'domain_frontend': settings.DOMAIN_FRONTEND,
            'activation_key': self.activation_key,
            'activation_message': self.activation_message
        })

        return context

    def activation(self, key):
        self.activation_message = ''
        self.activation_key = ActivationKeyModule.get_key(key)

        if self.activation_key:
            # User verified.
            self.activation_key.user.is_verified = True
            self.activation_key.user.save()

            # Key disabled.
            self.activation_key.is_used = True
            self.activation_key.save()

            self.activation_message = _('Activation is successfully completed.')
        else:
            self.activation_message = _('Incorrect key!')


class ResetPasswordView(TemplateView):
    template_name = 'reset-password.html'

    def dispatch(self, request, key, *args, **kwargs):
        self.reset_password_message = ''
        self.reset_password_key = None
        self.reset_password_error = False
        self.reset_password_success = False
        self.check_key(key)

        if not self.reset_password_key:
            self.reset_password_error = True

        return super(ResetPasswordView, self).dispatch(
            request, key, *args, **kwargs
        )

    def get_context_data(self, **kwargs):
        context = super(ResetPasswordView, self).get_context_data(**kwargs)

        context.update({
            'title': _('Reset Password'),
            'domain_frontend': settings.DOMAIN_FRONTEND,
            'reset_password_key': self.reset_password_key,
            'reset_password_error': self.reset_password_error,
            'reset_password_success': self.reset_password_success,
            'reset_password_message': self.reset_password_message,
            'reset_password_form': ResetPasswordForm(
                prefix=RESET_PASSWORD_FORM_PREFIX
            )
        })

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()

        if RESET_PASSWORD_FORM_PREFIX in request.POST:
            reset_password_form = ResetPasswordForm(
                self.request.POST, prefix=RESET_PASSWORD_FORM_PREFIX
            )

            if reset_password_form.is_valid():
                user = reset_password_form.save(self.reset_password_key)

                if not user:
                    self.reset_password_error = True
                else:
                    self.reset_password_success = True
                    self.reset_password_message = _(
                        _('Your password has been successfully determined.')
                    )

            context.update({
                'reset_password_form': reset_password_form,
                'reset_password_error': self.reset_password_error,
                'reset_password_success': self.reset_password_success,
                'reset_password_message': self.reset_password_message
            })

        return super(ResetPasswordView, self).render_to_response(context)

    def check_key(self, key):
        self.reset_password_key = ResetPasswordKeyModule.get_key(key)

        if not self.reset_password_key:
            self.reset_password_message = _('Incorrect or used key!')
