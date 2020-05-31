import csv
import re
import logging
log = logging.getLogger(__name__)

class CSVReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.volumes = [[0 for y in range(8)] for x in range(12)]

    # read in CSV file and output as a 12 by 8 array of volumes
    def readCSV(self):

        # read in the CSV file
        with open(self.csv_file) as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:
                well = row[0].strip()

                if not self.isValidWell(well):
                    log.info('Skipping cell "' + well + '"')
                    continue

                volume = int(row[1].strip())
                wellX = int(well[1:])-1
                # 32 is the difference between the unicode value of 'a' and 'A'
                wellY = (ord(well[0])-ord('A'))%32
                self.volumes[wellX][wellY] = volume

    def isValidWell(self, well_text):
        well_format = re.compile('[a-zA-Z][0-9]')
        return well_format.match(well_text)

    def getVolumes(self):
        return self.volumes
