# Third-Party
from rest_framework import viewsets, mixins, status
from djoser.views import TokenCreateView
from djoser import utils
from rest_framework.response import Response

# Django
from djoser.conf import settings

# Local Django
from users.models import User
from core.models import Contact
from Mudek.modules import MailModule
from core.serializers import (
    ContactSerializer, ContactCreateSerializer,
    TokenCreateSerializer
)


class TokenCreateView(TokenCreateView):
    serializer_class = TokenCreateSerializer

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = settings.SERIALIZERS.token
        return Response(
            data=token_serializer_class(token).data, status=status.HTTP_200_OK
        )


class ContactViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ContactCreateSerializer
        else:
            return ContactSerializer

    def get_permissions(self):
        permissions = super(ContactViewSet, self).get_permissions()

        if self.action == 'create':
            return []

        return permissions

    def perform_create(self, serializer):
        contact = serializer.save()

        # Send Contact Mail
        users = User.objects.filter(is_superuser=True)
        for user in users:
            MailModule.send_contact_mail(contact, user)