from django.test import TestCase
import datetime
from django.utils import timezone
from core.templatetags import custom_filters

class TimeMasksTests(TestCase):
    def test_date_mask(self):
        test_date = datetime.date(2017, 11, 21)
        self.assertEqual(custom_filters.date_mask(test_date), "21/11/2017")

    def test_datefull_mask(self):
        test_date = datetime.date(2017, 11, 21)
        self.assertEqual(custom_filters.datefull_mask(test_date), "21 de Novembro de 2017")

    def test_datetime_mask(self):
        test_date = datetime.datetime(2017, 11, 21, 22, 45, 00, 0, tzinfo=None)
        self.assertEqual(custom_filters.datetime_mask(test_date), "21/11/2017 22:45")
