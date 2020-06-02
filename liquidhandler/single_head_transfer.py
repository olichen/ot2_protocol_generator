from opentrons import protocol_api
import csv
import re

metadata = {
    'protocolName': 'Single head transfer',
    'author': 'Oliver Chen <olichen@ucdavis.edu',
    'description': 'Read in volumes from a CSV file and transfer volumes',
    'apiLevel': '2.2'
}

CUSTOM_PLATE = 'appliedbiosystems_96_wellplate_100ul'
CSV_FILE = 'SingleHeadTransfer.csv'

def run(protocol: protocol_api.ProtocolContext):

    volumes = readCSV(CSV_FILE)

    tiprack = protocol.load_labware('geb_96_tiprack_10ul', 1)
    plate1 = protocol.load_labware(CUSTOM_PLATE, 2)
    plate2 = protocol.load_labware(CUSTOM_PLATE, 3)

    p10 = protocol.load_instrument('p10_single', mount='right', tip_racks=[tiprack])

    for x in range(12):
        for y in range(8):
            well = chr(ord('A')+y) + str(x+1)
            p10.transfer(volumes[x][y], plate1[well], plate2[well])

# read in CSV file and output as a 12 by 8 array of volumes
def readCSV(csvname):
    volumes = [[0 for y in range(8)] for x in range(12)]

    # read in the CSV file
    with open(csvname) as csvfile:
        reader = csv.reader(csvfile)
        wellFormat = re.compile('[a-zA-Z][0-9]')

        for row in reader:
            well = row[0].strip()
            # check to make sure well is correctly formatted
            if not wellFormat.match(well):
                print('Skipping cell "' + well + '"')
                continue
    
            wellX = int(well[1:])-1
            # 32 is the difference between the unicode value of 'a' and 'A'
            wellY = (ord(well[0])-ord('A'))%32
            volume = int(row[1].strip())
            volumes[wellX][wellY] = volume

    return volumes
