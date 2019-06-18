# Third-Party
from rest_framework import serializers
from djoser.serializers import TokenCreateSerializer

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import Contact


class TokenCreateSerializer(TokenCreateSerializer):
    extra_error_messages = {
        'unverified_account': _('User account is unverified.')
    }

    def validate(self, attrs):
        super(TokenCreateSerializer, self).validate(attrs)

        self._validate_user_is_verified(self.user)

        return attrs

    def _validate_user_is_verified(self, user):
        if not self.user.is_verified:
            raise serializers.ValidationError(
                self.extra_error_messages['unverified_account']
            )


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'message', 'admin_read')


class ContactCreateSerializer(ContactSerializer):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
