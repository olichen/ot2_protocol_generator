from context import liquidhandler
from liquidhandler import csv_reader

import unittest

class TestCSVReader(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
    
    def test_isValidWell(self):
        csvr = csv_reader.CSVReader('placeholder')
        self.assertFalse(csvr.isValidWell('AA1'))
        self.assertFalse(csvr.isValidWell('A111'))
        self.assertFalse(csvr.isValidWell('A0'))
        self.assertFalse(csvr.isValidWell('A13'))
        self.assertFalse(csvr.isValidWell('i1'))
        self.assertFalse(csvr.isValidWell('I1'))
        self.assertTrue(csvr.isValidWell('A1'))
        self.assertTrue(csvr.isValidWell('A9'))
        self.assertTrue(csvr.isValidWell('A10'))
        self.assertTrue(csvr.isValidWell('A12'))
        self.assertTrue(csvr.isValidWell('a1'))
        self.assertTrue(csvr.isValidWell('a1'))
        self.assertTrue(csvr.isValidWell('h12'))
        self.assertTrue(csvr.isValidWell('h12'))
        self.assertTrue(csvr.isValidWell('A1'))
        self.assertTrue(csvr.isValidWell('A12'))
        self.assertTrue(csvr.isValidWell('H1'))
        self.assertTrue(csvr.isValidWell('H12'))


if __name__ == '__main__':
    unittest.main()
