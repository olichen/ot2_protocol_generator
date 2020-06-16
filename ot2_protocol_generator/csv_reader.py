import csv
import re
import logging
log = logging.getLogger()


# Reads a CSV file and returns a dict of 'well': 'volume'
class CSVReader:
    def __init__(self, csv_file):
        self.volumes = {}
        self.readCSV(csv_file)

    # Read in the CSV file
    def readCSV(self, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                well, volume = self.readRow(row)
                if well and volume:
                    self.volumes[well] = volume

    # Reads in a row; returns the tuple (well, volume) on a valid row.
    # Returns (None, None) on an invalid row.
    def readRow(self, row):
        # Try to access both cells. Fails on empty cell.
        try:
            well = row[0].strip()
            volume = row[1].strip()
        except IndexError:
            log.warning('Invalid cells ' + str(row) + '.')
            return None, None

        # Check to make sure we have a valid well position.
        if not self.isValidWell(well):
            log.warning("Invalid well '" + well + "'.")
            return None, None

        # Check if the well is already defined
        # Raises an exception if wells overlap
        if well in self.volumes:
            err_str = "Well '{0}' is already defined.".format(well)
            raise ValueError(err_str)

        # Check to make sure we have a valid voume
        # Raises an exception if we don't
        if not self.isValidVolume(volume):
            err_str = "Encountered invalid volume '{0}'.".format(volume)
            raise ValueError(err_str)

        return well, volume

    # Check to make sure each row is valid
    def isValidWell(self, well_text):
        well_format = re.compile('[A-H]([1-9]|(1[0-2]))')
        return well_format.fullmatch(well_text)

    # Check to make sure the volume is valid
    def isValidVolume(self, volume_text):
        try:
            int(volume_text)
            return True
        except ValueError:
            return False
