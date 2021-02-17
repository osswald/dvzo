from django.test import TestCase
from django.test import Client
from train_management.tests.helpers import SetupHelper
from train_management.models import Train
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

    def test_rest_endpoint_to_get_dayplanning(self):
        response = self.client.get(reverse('day-plannings'))

        expected = [
            {
                'id': 1,
                'label': 'Default label dayplanning',
                'date': '2021-02-13',
                'type': 'extra',
                'vehicles': [
                    {
                        'vehicle_type': 'engine',
                        'vehicle_label': 'Loki Elisabeth'
                    },
                    {
                        'vehicle_type': 'carriage',
                        'vehicle_label': 'Wagen Lisa'
                    },
                    {
                        'vehicle_type': 'carriage',
                        'vehicle_label': 'Wagen Peter'
                    },
                    {
                        'vehicle_type': 'carriage',
                        'vehicle_label': 'Wagen Emma'
                    }
                ]
            }
        ]

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json(), expected)

    def login(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
        self.client.login(**self.credentials)
