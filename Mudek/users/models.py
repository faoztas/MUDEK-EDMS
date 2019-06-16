# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

# Local Django
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # Base
    email = models.EmailField(
        verbose_name=_('Email'), max_length=255, unique=True
    )
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)

    # Permissions
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)
    is_verified = models.BooleanField(
        verbose_name=_('Verified'), default=False
    )
    is_academician = models.BooleanField(
        verbose_name=_('Academician'), default=True
    )
    is_department_manager = models.BooleanField(
        verbose_name=_('Department Manager'), default=False
    )
    is_assistant_department_manager = models.BooleanField(
        verbose_name=_('Assistant Department Manager'), default=False
    )
    is_dean_manager = models.BooleanField(
        verbose_name=_('Dean Manager'), default=False
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    def get_short_name(self):
        return '{first_name}'.format(first_name=self.first_name)


class ActivationKey(models.Model):
    key = models.CharField(verbose_name=_('Key'), max_length=50, unique=True)
    is_used = models.BooleanField(verbose_name=_('Used'), default=False)
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL, related_name='activation_keys',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Activation Key')
        verbose_name_plural = _('Activation Keys')

    def __str__(self):
        return '{key}'.format(key=self.key)


class ResetPasswordKey(models.Model):
    key = models.CharField(verbose_name=_('Key'), max_length=50, unique=True)
    is_used = models.BooleanField(verbose_name=_('Used'), default=False)
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL, related_name='reset_password_keys',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Reset Password Key')
        verbose_name_plural = _('Reset Password Keys')

    def __str__(self):
        return '{key}'.format(key=self.key)
