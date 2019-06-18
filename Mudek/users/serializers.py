# Third-Party
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

# Django
from django.conf import settings
from django.contrib.auth import password_validation

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'is_active', 'is_verified',  'is_academician',
            'is_department_manager', 'is_assistant_department_manager',
            'is_dean_manager'
        )


class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserRetrieveSerializer(UserSerializer):
    pass


class UserCreateSerializer(UserSerializer):
    confirm_password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name',
            'last_name', 'password', 'confirm_password'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        if value != self.initial_data.get('confirm_password', None):
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(value)

        return value


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        fields = ('old_password', 'new_password', 'confirm_new_password')

    def validate_confirm_new_password(self, value):
        if value != self.initial_data['new_password']:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(value)

        return value

    def validate_old_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError(_(
                'Your old password was entered incorrectly. '
                'Please enter it again.'
            ))

        return value


class UserPasswordForgotSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)

    def validate_email(self, value):
        self.user = None
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(_('User not found!'))

        return value


class UserActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)

    def validate_email(self, value):
        self.user = None
        try:
            self.user = User.objects.get(email=value)

            if self.user.is_verified:
                raise serializers.ValidationError(_('User already verifed!'))
        except User.DoesNotExist:
            raise serializers.ValidationError(_('User not found!'))

        return value
