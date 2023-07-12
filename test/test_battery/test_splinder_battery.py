import unittest
from datetime import date

from battery.splinder_battery import SplinderBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        current_date = date.fromisoformat("2023-07-12")
        last_service_date = date.fromisoformat("2019-06-11")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_no_needs_service(self):
        current_date = date.fromisoformat("2023-07-12")
        last_service_date = date.fromisoformat("2020-06-11")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())