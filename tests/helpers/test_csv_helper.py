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

    def test__readRow(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        self.assertEqual(csvr._readRow(2, ['a', '1']), (None, None))
        self.assertEqual(csvr._readRow(2, ['garbage', '1']), (None, None))
        self.assertEqual(csvr._readRow(2, ['H2']), (None, None))
        with self.assertRaises(ValueError):
            csvr._readRow(2, ['A1', 'garbage'])
        with self.assertRaises(ValueError):
            csvr._readRow(2, ['C2', ''])
        self.assertEqual(csvr._readRow(2, ['H1', ' 4 ']), ('H1', '4'))

    def test__is_valid_volume(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        self.assertFalse(csvr._is_valid_volume(''))
        self.assertFalse(csvr._is_valid_volume(' '))
        self.assertFalse(csvr._is_valid_volume('text'))
        self.assertFalse(csvr._is_valid_volume('a2'))
        self.assertFalse(csvr._is_valid_volume('1.2.3'))
        self.assertFalse(csvr._is_valid_volume('1 .2'))
        self.assertTrue(csvr._is_valid_volume(' 1'))
        self.assertTrue(csvr._is_valid_volume('1'))
        self.assertTrue(csvr._is_valid_volume('1 '))
        self.assertTrue(csvr._is_valid_volume('1.23 '))

    def test__well_to_int(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        well_x = [str(x) for x in range(1, 13)]
        well_y = [chr(x) for x in range(ord('A'), ord('A')+8)]
        for i, well in enumerate(y + x for x in well_x for y in well_y):
            self.assertEqual(csvr._well_to_int(well), i)
        self.assertEqual(csvr._well_to_int('A1'), 0)
        self.assertEqual(csvr._well_to_int('B1'), 1)
        self.assertEqual(csvr._well_to_int('A2'), 8)
        self.assertEqual(csvr._well_to_int('B2'), 9)
        self.assertEqual(csvr._well_to_int('G12'), 94)
        self.assertEqual(csvr._well_to_int('H12'), 95)
        self.assertEqual(csvr._well_to_int('a1'), None)
        self.assertEqual(csvr._well_to_int('a5'), None)

    def test__is_valid_well(self):
        csvr = csv_helper.CSVReader(self.temp_csv)
        well_x = [str(x) for x in range(1, 13)]
        well_y = [chr(x) for x in range(ord('A'), ord('A')+8)]
        for well in (y + x for x in well_x for y in well_y):
            self.assertTrue(csvr._is_valid_well(well))
        self.assertFalse(csvr._is_valid_well('AA1'))
        self.assertFalse(csvr._is_valid_well('A111'))
        self.assertFalse(csvr._is_valid_well('A0'))
        self.assertFalse(csvr._is_valid_well('A13'))
        self.assertFalse(csvr._is_valid_well('I1'))
        self.assertFalse(csvr._is_valid_well('a1'))
        self.assertFalse(csvr._is_valid_well('a12'))


if __name__ == '__main__':
    unittest.main()
