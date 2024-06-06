from datetime import datetime
from unittest import TestCase
from .l2l_extras import format_date


class TestL2LExtras(TestCase):
    from_format = "%Y-%m-%dT%H:%M:%S"
    to_format = "%Y-%m-%d %H:%M:%S"

    def test_when_str_date_then_ok(self):
        now = datetime.now()
        self.assertEqual(
            format_date(now.strftime(self.from_format)), now.strftime(self.to_format)
        )

    def test_when_datetime_then_ok(self):
        now = datetime.now()
        self.assertEqual(format_date(now), now.strftime(self.to_format))

    def test_when_not_str_date_then_emtpy_str(self):
        self.assertEqual(format_date("foo"), "")
        self.assertEqual(format_date(None), "")
        self.assertEqual(format_date(10), "")
        self.assertEqual(format_date({"foo": "bar"}), "")
        self.assertEqual(format_date([1, 2, 3]), "")

    def test_when_str_not_in_expected_format_then_empty_str(self):
        now = datetime.now()
        now_str = now.strftime("%Y-%m")
        self.assertEqual(format_date(now_str), "")
