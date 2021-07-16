from train_management.tests.base import DvzoTestCase


class TestDayPlanning(DvzoTestCase):
    def setUp(self):
        super(TestDayPlanning, self).setUp()
        # add additional test data
        self.add_test_data()

    def test_dayplanning_overview_shows_dayplanning_one(self):
        self.login()
        self.add_permissions(["view_dayplanning"])

        # get all hrefs in the day planning view
        response = self.client.get("/dayplanning/")
        hrefs = self.resolve_xpath(response, "//a/@href")

        # it is expected that there is the day planning one since we added it with the test data
        self.assertIn("/dayplanning/detail/1/", hrefs)

    def test_dayplanning_one_view(self):
        self.login()
        self.add_permissions(["view_dayplanning"])

        # extract the day plannings table cells text
        response = self.client.get("/dayplanning/detail/1/")
        table_cells_text = self.resolve_xpath(response, "//table/tbody/tr/td/text()")

        # it is expected that the date of the day planning is the 13th of Feb and visible in the table
        self.assertIn("13. Februar 2021", table_cells_text)
