import csv
import re
import logging


# Reads a CSV file and returns a list of all 96 volumes
class CSVReader:
    def __init__(self, csv_file):
        self.volumes = {}
        self._logger = logging.getLogger()
        try:
            self._readCSV(csv_file)
        except FileNotFoundError:
            raise FileNotFoundError("Please select a valid CSV file")

    # Read in the CSV file
    def _readCSV(self, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader, 1):
                well, volume = self._readRow(i, row)
                if well and volume:
                    self.volumes[well] = volume

    # Reads in a row; returns the tuple (well, volume) as strings
    # Returns a warning and (None, None) or an exception on an invalid row
    def _readRow(self, rownum, row):
        # Warning if there aren't at least 2 cells in the row
        try:
            well = row[0].strip()
            vol = row[1].strip()
        except IndexError:
            err_str = f"Row {rownum}: Invalid cells '{row}'"
            self._logger.warning(err_str)
            return None, None

        # Warning for invalid well
        if not self._is_valid_well(well):
            if not rownum == 1:
                err_str = f"Row {rownum}: Invalid well '{well}'"
                self._logger.warning(err_str)
            return None, None

        # Exception for volumes that are defined twice
        if well in self.volumes:
            err_str = "Error: Well '{well}' in row {rownum} is already defined"
            raise ValueError(err_str)

        # Exception for invalid volumes
        if not self._is_valid_volume(vol):
            err_str = f"Error: Invalid volume '{vol}' in row {rownum}"
            raise ValueError(err_str)

        # Warning if there are too many decimal places
        if vol[::-1].find('.') > 1:
            err_str = f"Row {rownum}: '{vol}' longer than one decimal place"
            self._logger.warning(err_str)

        # Warning if volume is too large
        if float(vol) > 10:
            err_str = f"Row {rownum}: Volume '{vol}' > 10 μL",
            self._logger.warning(err_str)

        return well, vol

    # Converts a text well to an int
    # A1 => 0, B1 => 2, ..., H11 => 94, H12 => 95
    def _well_to_int(self, well):
        if not self._is_valid_well(well):
            return None
        pos = 8 * (int(well[1:]) - 1)
        pos += ord(well[0]) - ord('A')
        return pos

    # Check well name against regex (A-H followed by 1-12)
    def _is_valid_well(self, well_text: str) -> bool:
        well_format = re.compile('[A-H]([1-9]|(1[0-2]))')
        return well_format.fullmatch(well_text)

    # Check to make sure the volume is valid
    def _is_valid_volume(self, volume_text: str) -> bool:
        try:
            float(volume_text)
            return True
        except ValueError:
            return False
