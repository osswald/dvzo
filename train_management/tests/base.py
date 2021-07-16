from django.contrib.auth.models import Permission
from django.http import HttpResponse
from django.test import Client
from django.test import TestCase
from lxml import html  # nosec

from train_management.tests.helpers import SetupHelper
from users.models import User


class DvzoTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_user()

    def create_user(self):
        """Create test user with the credentials
        username: username
        password: secret
        """
        self.credentials = {"username": "testuser", "password": "secret"}
        self.user = User.objects.create(username=self.credentials["username"])
        self.user.set_password(self.credentials["password"])
        self.user.save()

    def login(self):
        """Login the test user."""
        self.client.login(**self.credentials)

    def add_permissions(self, permissions):
        """Add a permissions by codename.
        param permissions: str or list object with the permissions code names.
        """
        if isinstance(permissions, str):
            permissions = [permissions]
        for permission in permissions:
            self.user.user_permissions.add(Permission.objects.filter(codename=permission).first())
        self.user.save()

    @staticmethod
    def resolve_xpath(response: HttpResponse, xpath: str):
        """This method resolves a given xpath from the http response.
        Example xpath: "//div[@class='card-title']/text()"
        The example xpath would search for div elements with class 'card-title' and return their text
        as a list.
        """
        tree = html.fromstring(response.content)
        return tree.xpath(xpath)

    @staticmethod
    def add_test_data():
        setup_helper = SetupHelper()
        setup_helper.create_train_components()
        day_planning_1 = setup_helper.get_day_planning()
        train_1 = setup_helper.get_train(day_planning_1)
        setup_helper.create_train_config(train_1)
