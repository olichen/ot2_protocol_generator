import csv
import re
import logging


# Reads a CSV file and returns a dict of 'well': 'volume'
class CSVReader:
    def __init__(self, csv_file):
        self.volumes = {}
        self.logger = logging.getLogger()
        self.readCSV(csv_file)

    # Read in the CSV file
    def readCSV(self, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)

            for i, row in enumerate(reader):
                well, volume = self.readRow(i+1, row)
                if well and volume:
                    self.volumes[well] = volume

    # Reads in a row; returns the tuple (well, volume) on a valid row.
    # Returns (None, None) on an invalid row.
    def readRow(self, rownum, row):
        # Try to access both cells. Fails on empty cell.
        try:
            well = row[0].strip()
            volume = row[1].strip()
        except IndexError:
            err_str = str.format(
                    "Warning: " +
                    "Invalid cells '{0}' in row {1}",
                    row, rownum)
            self.logger.warning(err_str)
            return None, None

        # Check to make sure we have a valid well position.
        if not self.isValidWell(well):
            if not rownum == 1:
                err_str = str.format(
                        "Warning: " +
                        "Invalid well '{0}' in row {1}",
                        well, rownum)
                self.logger.warning(err_str)
            return None, None

        # Check if the well is already defined
        # Raises an exception if wells overlap
        if well in self.volumes:
            err_str = str.format(
                    "Error: " +
                    "Well '{0}' in row {1} is already defined elsewhere",
                    well, rownum)
            raise ValueError(err_str)

        # Check to make sure we have a valid volume
        # Raises an exception if we don't
        if not self.isValidVolume(volume):
            err_str = str.format(
                    "Error: " +
                    "Encountered invalid volume '{0}' in row {1}",
                    volume, rownum)
            raise ValueError(err_str)

        if volume[::-1].find('.') > 1:
            err_str = str.format(
                    "Warning: " +
                    "Volume '{0}' in row {1} has more than one decimal place",
                    volume, rownum)
            self.logger.warning(err_str)

        if float(volume) > 10:
            err_str = str.format(
                    "Warning: " +
                    "Volume '{0}' in row {1} is greater than 10 μL",
                    volume, rownum)
            self.logger.warning(err_str)

        return well, volume

    # Check to make sure each row is valid
    def isValidWell(self, well_text):
        well_format = re.compile('[A-H]([1-9]|(1[0-2]))')
        return well_format.fullmatch(well_text)

    # Check to make sure the volume is valid
    def isValidVolume(self, volume_text):
        try:
            float(volume_text)
            return True
        except ValueError:
            return False
