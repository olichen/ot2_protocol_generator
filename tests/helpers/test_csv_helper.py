from ot2_protocol_generator.helpers import csv_helper

import unittest
import os
import csv


class TestCSVHelper(unittest.TestCase):
    def setUp(self):
        self.temp_csv = os.path.join(os.path.dirname(__file__), 'temp.csv')
        with open(self.temp_csv, 'w') as file:
            csv.writer(file)

    def writeRowToTempCSV(self):
        with open(self.temp_csv, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['abc'])
            writer.writerow(['def'])

    def tearDown(self):
        os.remove(self.temp_csv)

    def test_init(self):
        with self.assertRaises(FileNotFoundError):
            csv_helper.CSVReader('no_file.csv')
        with self.assertRaises(IsADirectoryError):
            csv_helper.CSVReader('/')

    def test_readRow(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        self.assertEqual(csvr.readRow(2, ['a', '1']), (None, None))
        self.assertEqual(csvr.readRow(2, ['garbage', '1']), (None, None))
        self.assertEqual(csvr.readRow(2, ['H2']), (None, None))
        with self.assertRaises(ValueError):
            csvr.readRow(2, ['A1', 'garbage'])
        with self.assertRaises(ValueError):
            csvr.readRow(2, ['C2', ''])
        self.assertEqual(csvr.readRow(2, ['H1', ' 4 ']), ('H1', '4'))

    def test_isValidWell(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        for i in range(ord('A'), ord('H')):
            for j in range(1, 12):
                self.assertTrue(csvr.isValidWell(chr(i)+str(j)))
        self.assertFalse(csvr.isValidWell('AA1'))
        self.assertFalse(csvr.isValidWell('A111'))
        self.assertFalse(csvr.isValidWell('A0'))
        self.assertFalse(csvr.isValidWell('A13'))
        self.assertFalse(csvr.isValidWell('I1'))
        self.assertFalse(csvr.isValidWell('a1'))
        self.assertFalse(csvr.isValidWell('a12'))

    def test_isValidVolume(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        self.assertFalse(csvr.isValidVolume(''))
        self.assertFalse(csvr.isValidVolume(' '))
        self.assertFalse(csvr.isValidVolume('text'))
        self.assertFalse(csvr.isValidVolume('a2'))
        self.assertTrue(csvr.isValidVolume(' 1'))
        self.assertTrue(csvr.isValidVolume('1'))
        self.assertTrue(csvr.isValidVolume('1 '))


if __name__ == '__main__':
    unittest.main()
