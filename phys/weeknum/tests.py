from django.test import TestCase
from .functions import *


class TestFunction(TestCase):
    def test_get_count_week_year(self):
        number = get_count_weeks_year(date(2019, 1, 1))
        self.assertEqual(number, 1)

    def test_get_total_count_week_year(self):
        year = 2020
        number = get_total_count_weeks_year(year)
        self.assertEqual(number, 53)

    def test_get_total_count_weeks(self):
        start_date = date(2019, 1, 1)
        user_date = date(2019, 1, 6)
        number = get_total_count_weeks(user_date, start_date)
        self.assertEqual(number, 2)
