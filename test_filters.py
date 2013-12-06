# -*- coding: utf-8 -*-

import unittest
from filters.english import *

class TestEnglishFilter(unittest.TestCase):
    def test_has_japanese(self):
        self.assertFalse(has_japanese('<entry></entry>'))
        self.assertTrue(has_japanese('<entry xmlns="http://www.w3.org/2005/Atom"><summary>あいうえお</summary></entry>'))
