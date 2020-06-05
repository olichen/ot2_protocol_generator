from context import liquidhandler
from liquidhandler import csv_reader

import unittest


class TestCSVReader(unittest.TestCase):
    def setUp(self):
        self.CSV_FILE = 'empty_csv.csv'
        self.csvr = csv_reader.CSVReader(self.CSV_FILE)

    def test_init(self):
        with self.assertRaises(FileNotFoundError):
            csv_reader.CSVReader('no_file.csv')
        # self.assertEqual(self.csvr.volumes, {})

    def test_readRow(self):
        self.assertFalse(self.csvr.readRow(['a','1']))
        self.assertFalse(self.csvr.readRow(['H2']))
        self.assertFalse(self.csvr.readRow(['A1', 'garbage']))
        self.assertFalse(self.csvr.readRow(['garbage', '1']))
        self.assertFalse(self.csvr.readRow(['C2', '']))
        self.assertEqual(self.csvr.readRow(['H1', ' 4 ']), ('H1', 4))

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

    def test_isValidVolume(self):
        self.assertFalse(self.csvr.isValidVolume(''))
        self.assertFalse(self.csvr.isValidVolume(' '))
        self.assertFalse(self.csvr.isValidVolume('text'))
        self.assertFalse(self.csvr.isValidVolume('a2'))
        self.assertTrue(self.csvr.isValidVolume(' 1'))
        self.assertTrue(self.csvr.isValidVolume('1'))
        self.assertTrue(self.csvr.isValidVolume('1 '))


if __name__ == '__main__':
    unittest.main()
