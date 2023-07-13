import unittest

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_lights = True
        engine = SternmanEngine(warning_lights)
        self.assertTrue(engine.needs_service())

    def test_no_needs_service(self):
        warning_lights = False
        engine = SternmanEngine(warning_lights)
        self.assertFalse(engine.needs_service())