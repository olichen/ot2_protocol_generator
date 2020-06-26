from ot2_protocol_generator.helpers import multi_transfer_helper as mth

import unittest


class TestMultiTransferHelper(unittest.TestCase):
    def setUp(self):
        self.volumedict = {
                'A1': '1', 'B1': '1', 'C1': '1', 'D1': '1',
                'E1': '1', 'F1': '1', 'G1': '1', 'H1': '1',
                'A2': '2', 'B2': '2', 'C2': '2', 'D2': '2',
                'E2': '2', 'F2': '2', 'G2': '2', 'H2': '2',
                'A3': '3', 'B3': '3', 'C3': '3', 'D3': '3',
                'E3': '3', 'F3': '3', 'G3': '3', 'H3': '3',
                'A4': '4', 'B4': '4', 'C4': '4', 'D4': '4',
                'E4': '4', 'F4': '4', 'G4': '4', 'H4': '4',
                'A5': '5', 'B5': '5', 'C5': '5', 'D5': '5',
                'E5': '5', 'F5': '5', 'G5': '5', 'H5': '5',
                'A6': '6', 'B6': '6', 'C6': '6', 'D6': '6',
                'E6': '6', 'F6': '6', 'G6': '6', 'H6': '6',
                'A7': '7', 'B7': '7', 'C7': '7', 'D7': '7',
                'E7': '7', 'F7': '7', 'G7': '7', 'H7': '7',
                'A8': '8', 'B8': '8', 'C8': '8', 'D8': '8',
                'E8': '8', 'F8': '8', 'G8': '8', 'H8': '8',
                'A9': '9', 'B9': '9', 'C9': '9', 'D9': '9',
                'E9': '9', 'F9': '9', 'G9': '9', 'H9': '9',
                'A10': '10', 'B10': '10', 'C10': '10', 'D10': '10',
                'E10': '10', 'F10': '10', 'G10': '10', 'H10': '10',
                'A11': '11', 'B11': '11', 'C11': '11', 'D11': '11',
                'E11': '11', 'F11': '11', 'G11': '11', 'H11': '11',
                'A12': '12', 'B12': '12', 'C12': '12', 'D12': '12',
                'E12': '12', 'F12': '12', 'G12': '12', 'H12': '12',
                }

    def testMultiTransferHelper(self):
        try:
            mth.MultiTransferHelper(self.volumedict)
        except Exception:
            self.fail('Unexpected exception')

        self.volumedict['A1'] = '11'
        with self.assertRaises(ValueError):
            mth.MultiTransferHelper(self.volumedict)

        del self.volumedict['A1']
        with self.assertRaises(IndexError):
            mth.MultiTransferHelper(self.volumedict)

    def testCharToInt(self):
        et = mth.MultiTransferHelper(self.volumedict)
        self.assertEqual(et.charToInt('A'), 0)
        self.assertEqual(et.charToInt('B'), 1)
        self.assertEqual(et.charToInt('C'), 2)
        self.assertEqual(et.charToInt('D'), 3)
        self.assertEqual(et.charToInt('E'), 4)
        self.assertEqual(et.charToInt('F'), 5)
        self.assertEqual(et.charToInt('G'), 6)
        self.assertEqual(et.charToInt('H'), 7)


if __name__ == '__main__':
    unittest.main()
