from ot2_protocol_generator.gui import plate_data
from ot2_protocol_generator.gui import config

import unittest


class TestPlateData(unittest.TestCase):
    def setUp(self):
        self.cfg = config.Configuration('null')
        self.data = plate_data.PlateData(
                tip_rack_name=self.cfg['TIP_RACK_NAMES'][0],
                tip_rack_loc=self.cfg['TIP_RACK_LOCS'][0],
                src_plate_name=self.cfg['PLATE_NAMES'][0],
                src_plate_loc=self.cfg['PLATE_LOCS'][0],
                dest_plate_name=self.cfg['PLATE_NAMES'][0],
                dest_plate_loc=self.cfg['PLATE_LOCS'][0],
                csv_file_loc='')

    def test_isValid(self):
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.pipette_type = 'single'
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.csv_file_loc = '/placeholder.py'
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.src_plate_loc = self.cfg['PLATE_LOCS'][1]
        with self.assertRaises(ValueError):
            self.data.isValid()

        self.data.dest_plate_loc = self.cfg['PLATE_LOCS'][2]
        self.assertTrue(self.data.isValid())

    def test_checkMissingInput(self):
        with self.assertRaises(ValueError):
            self.data.checkMissingInput()

        self.data.pipette_type = 'single'
        with self.assertRaises(ValueError):
            self.data.checkMissingInput()

        self.data.csv_file_loc = '/placeholder.py'
        try:
            self.data.checkMissingInput()
        except Exception:
            self.fail('Unexpected exception')

    def test_checkPlateLocations(self):
        with self.assertRaises(ValueError):
            self.data.checkPlateLocations()

        self.data.src_plate_loc = self.cfg['PLATE_LOCS'][1]
        with self.assertRaises(ValueError):
            self.data.checkPlateLocations()

        self.data.dest_plate_loc = self.cfg['PLATE_LOCS'][2]
        try:
            self.data.checkPlateLocations()
        except Exception:
            self.fail('Unexpected exception')


if __name__ == '__main__':
    unittest.main()
