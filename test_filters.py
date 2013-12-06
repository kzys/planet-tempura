import unittest
from filters.english import *

class TestEnglishFilter(unittest.TestCase):
    def test_has_japanese(self):
        self.assertFalse(has_japanese('<entry></entry>'))
