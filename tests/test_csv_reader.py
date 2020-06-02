from context import liquidhandler
from liquidhandler import csv_reader

import unittest

class TestCSVReader(unittest.TestCase):
    def setUp(self):
        self.CSV_FILE = 'SingleHeadTransfer.csv'
        self.csvr = csv_reader.CSVReader(self.CSV_FILE)

    def test_init(self):
        self.assertEqual(self.csvr.volumes, {})
        self.assertEqual(self.csvr.csv_file, self.CSV_FILE)
    
    def test_isValidWell(self):
        for i in range(ord('A'), ord('H')):
            for j in range(1, 12):
                self.assertTrue(self.csvr.isValidWell(chr(i)+str(j)))
        self.assertFalse(self.csvr.isValidWell('AA1'))
        self.assertFalse(self.csvr.isValidWell('A111'))
        self.assertFalse(self.csvr.isValidWell('A0'))
        self.assertFalse(self.csvr.isValidWell('A13'))
        self.assertFalse(self.csvr.isValidWell('I1'))
        self.assertFalse(self.csvr.isValidWell('a1'))
        self.assertFalse(self.csvr.isValidWell('a12'))

if __name__ == '__main__':
    unittest.main()
