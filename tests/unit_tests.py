# -*- coding: utf-8 -*-
import unittest
import datetime
import time
import os
import sys
BASEDIR = os.path.abspath(os.path.join(
                          os.path.dirname(os.path.abspath(__file__)),
                          ".."))
sys.path.insert(0, BASEDIR)
import autolike
import locale

class TestAutolike(unittest.TestCase):
    def test_facebook(self):
        res = autolike.facebook()
        self.assertIsInstance(res, dict, "The return type is not a dictionary")
        
if __name__ == "__main__":
    unittest.main()
