# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DateModel(models.Model):
    create_date = models.DateTimeField(
        verbose_name=_('Create Date'), auto_now_add=True, editable=False
    )
    update_date = models.DateTimeField(
        verbose_name=_('Update Date'), auto_now=True, editable=False
    )

    class Meta:
        abstract = True


class Contact(DateModel):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email'), max_length=254)
    message = models.TextField(verbose_name=_('Message'))
    admin_read = models.BooleanField(_("Admin read?"), default=False)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = ('Contacts')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )
