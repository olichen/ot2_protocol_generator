import csv
import re
import logging
log = logging.getLogger(__name__)


class CSVReader:
    def __init__(self, csv_file):
        self.volumes = {}
        self.readCSV(csv_file)

    # read in the CSV file
    def readCSV(self, csv_file):

        # read in the CSV file
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                well, volume = self.readRow(row)
                if well and volume:
                    self.volumes[well] = volume

    def readRow(self, row):
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

        # Check if the well is already defined.
        if well in self.volumes:
            log.error("Well '" + well + "' is already defined.")
            return None, None

        # Check to make sure we have a valid volume.
        if not self.isValidVolume(volume):
            log.error("Encountered invalid volume '" + volume + "'.")
            return None, None

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
