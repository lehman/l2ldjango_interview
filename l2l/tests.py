from django.test import TestCase
from l2l.templatetags.l2l_filters import toDateAndTimeString
from datetime import datetime

class toDateAndTimeStringTestCase(TestCase):
    def test_datetime_param(self):
        """when given datetime object, returns string of correct format"""
        param = datetime(2024, 8, 30, 1, 2, 3)
        # result = now|toDateAndTimeString
        result = toDateAndTimeString(param)
        self.assertEqual(result, '2024-08-30 01:02:03')

    def test_string_param(self):
        """when given string, returns string of correct format"""
        param = "2024-01-15T21:41:28"
        # result = param|toDateAndTimeString
        result = toDateAndTimeString(param)
        self.assertEqual(result, '2024-01-15 21:41:28')
