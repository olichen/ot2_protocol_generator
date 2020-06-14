from context import ot2_protocol_generator
from ot2_protocol_generator import eight_transfer

import unittest


class TestEightTransfer(unittest.TestCase):
    def setUp(self):
        self.data = protocol_data.ProtocolData(
            tip_rack_type='',
            tip_rack_loc='',
            src_plate_type='',
            src_plate_loc='',
            dest_plate_type='',
            dest_plate_loc='',
            pipette_type='',
            pipette_loc='',
            csv_file_loc='')

    def test_isValid(self):
        with self.assertRaises(ValueError):
            self.data.isValid()
        self.data.tip_rack_type = 'a'
        self.data.tip_rack_loc = '1'
        with self.assertRaises(ValueError):
            self.data.isValid()
        self.data.src_plate_type = 'b'
        self.data.src_plate_loc = '2'
        with self.assertRaises(ValueError):
            self.data.isValid()
        self.data.dest_plate_type = 'c'
        self.data.dest_plate_loc = '3'
        with self.assertRaises(ValueError):
            self.data.isValid()
        self.data.pipette_type = 'd'
        self.data.pipette_loc = 'r'
        with self.assertRaises(ValueError):
            self.data.isValid()
        self.data.csv_file_loc = 'f'
        self.assertTrue(self.data.isValid())

if __name__ == '__main__':
    unittest.main()
