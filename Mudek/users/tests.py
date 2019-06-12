# Third-Party
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local Django
from users.models import User
from Mudek.modules import ActivationKeyModule


class UserAPITestCase(APITestCase):
    dummy_data = {
        'email': '',
        'first_name': '',
        'last_name': '',
        'password': ''
    }

    def setUp(self):
        # Create User and Token
        self.user = User.objects.create_user(
            email=self.dummy_data.get('email', None),
            password=self.dummy_data.get('password', None)
        )
        self.user.first_name = self.dummy_data.get('first_name', None)
        self.user.last_name = self.dummy_data.get('last_name', None)
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Create Activation Key
        self.activation_key = ActivationKeyModule.create_key(user=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
