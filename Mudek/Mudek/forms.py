# Django
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _

# Local Django
from users.models import User


class ResetPasswordForm(forms.Form):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
        strip=False,
        required=True,
        help_text=password_validation.password_validators_help_text_html(),
    )
    confirm_password = forms.CharField(
        label=_('Confirm Password'),
        widget=forms.PasswordInput,
        strip=False,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
            else:
                password_validation.validate_password(confirm_password)

        return self.cleaned_data

    def save(self, key, commit=True):
        user = None

        if commit:
            # Set Password
            user = key.user
            user.set_password(self.cleaned_data['password'])
            user.save()

            # Key Updated
            key.is_used = True
            key.save()

        return user
