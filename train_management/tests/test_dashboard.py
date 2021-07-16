from train_management.tests.base import DvzoTestCase


class TestDashboard(DvzoTestCase):
    def test_anonymous_user_is_redirected_to_login(self):
        # call the dashboard (url -> /)
        response = self.client.get("/")

        # it is expected that user who is not logged in will be redirect to the login page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/accounts/login/?next=/")

    def test_logged_in_user_can_view_dashboard(self):
        # login the testuser (self.user, instantiated in DvzoTestCase)
        self.login()
        # give this user the permissions required to view the dashboard.
        self.add_permissions(["view_dayplanning"])

        # call the dashboard (url -> /)
        response = self.client.get("/")

        # it is expected that the logged in user with the right permission can view the dashboard
        self.assertEqual(response.status_code, 200)

        # it is expected that the dashboard contains the titles below.
        titles = self.resolve_xpath(response, "//div[@class='card-title']/text()")
        self.assertEqual(
            titles,
            ['Nächste Fahrsonntage', 'Nächste Extrafahrten', 'Andere Fahrten', 'Frequenzen 2021',
             'Fehlende Einteilung', 'Fehlende Trassenbestellung', 'Was ist neu?'])
