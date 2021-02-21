from django.test import TestCase
from django.test import Client
from train_management.tests.helpers import SetupHelper
from train_management.models import Train
from train_management.views import get_day_planning_data
from django.contrib.auth.models import User
from django.urls import reverse


class AnimalTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.login()

        setup_helper = SetupHelper()
        setup_helper.create_train_components()
        day_planning_1 = setup_helper.get_day_planning()
        train_1 = setup_helper.get_train(day_planning_1)
        setup_helper.create_train_config(train_1)

    def login(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.login(**self.credentials)
