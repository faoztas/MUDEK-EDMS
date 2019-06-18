# Third-Party
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import detail_route, list_route
from djoser import utils

# Django
from django.core.mail import send_mail
from djoser.conf import settings

# Local Django
from users.models import User, ActivationKey
from Mudek.modules import (
    ActivationKeyModule, ResetPasswordKeyModule, MailModule
)
from users.serializers import (
    UserSerializer, UserListSerializer, UserCreateSerializer,
    UserRetrieveSerializer, UserUpdateSerializer,
    UserPasswordChangeSerializer, UserPasswordForgotSerializer,
    UserActivationResendSerializer
)


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'create':
            return UserCreateSerializer
        elif self.action == 'retrieve':
            return UserRetrieveSerializer
        elif self.action == 'update':
            return UserUpdateSerializer
        else:
            return UserSerializer

    def get_route_serializer_class(self):
        if self.action == 'change_password':
            return UserPasswordChangeSerializer
        elif self.action == 'forgot_password':
            return UserPasswordForgotSerializer
        elif self.action == 'resend_activation':
            return UserActivationResendSerializer
        else:
            return UserSerializer

    def get_permissions(self):
        permissions = super(UserViewSet, self).get_permissions()

        if self.action in ['create', 'forgot_password', 'resend_activation']:
            return []

        return permissions

    def perform_create(self, serializer):
        # Create User
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password', ''))
        user.save()

        # Create Activation Key
        activation_key = ActivationKeyModule.create_key(user=user)

        # Send Activation Mail
        MailModule.send_activation_mail(activation_key)

        return user

    @detail_route(methods=['post'], url_path='password/change',
                  url_name='change-password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        serializer_class = self.get_route_serializer_class()
        serializer = serializer_class(
            data=request.data, context={'user': user}
        )

        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    @list_route(methods=['post'], url_path='password/forgot',
                url_name='forgot-password')
    def forgot_password(self, request):
        serializer_class = self.get_route_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Create Forgot Password Key
            reset_password_key = ResetPasswordKeyModule.create_key(
                user=serializer.user
            )

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    @list_route(methods=['post'], url_path='activation/resend',
                url_name='resend-activation')
    def resend_activation(self, request):
        serializer_class = self.get_route_serializer_class()
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            # Create Activation Key
            activation_key = ActivationKeyModule.create_key(
                user=serializer.user
            )

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
