import csv
import re
import logging
log = logging.getLogger(__name__)


class CSVReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.volumes = {}
        self.readCSV()

    # read in CSV file and output as a 12 by 8 array of volumes
    def readCSV(self):

        # read in the CSV file
        with open(self.csv_file) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                well = row[0].strip()

                # Check to make sure the well position is valid
                if not self.isValidWell(well):
                    log.warning("Skipping cell '" + well + "'.")
                    continue

                # Check to make sure volumes are valid
                if well in self.volumes:
                    log.warning("Overwriting well '" + well + "'.")

                # Try to write the volume to the volumes dict
                try:
                    volume = int(row[1].strip())
                    self.volumes[well] = volume
                except:
                    log.error("Encountered invalid volume '" + volume + "'.")

    def isValidWell(self, well_text):
        well_format = re.compile('[A-H]([1-9]|(1[0-2]))')
        return well_format.fullmatch(well_text)

    def getVolumes(self):
        return self.volumes
