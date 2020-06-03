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

    # output each row to the hash map self.volumes
    def readRow(self, row):
        well = row[0].strip()
        volume = row[1].strip()

        # Check to make sure the well position is valid
        if not self.isValidWell(well):
            log.warning("Skipping cell " + str(row) + ".")
            return

        # Check if the well is already defined
        if well in self.volumes:
            log.error("Well '" + well + "' is already defined.")
            return

        # Try to write the volume to the volumes dict
        if self.isValidVolume(volume):
            return well, int(volume)

        return

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
            log.error("Encountered invalid volume '" + volume_text + "'.")
            return False
