from opentrons import protocol_api

metadata = {
    'protocolName': 'Single head transfer',
    'author': 'Oliver Chen <olichen@ucdavis.edu>',
    'description': 'Read in volumes from a CSV file and transfer volumes',
    'apiLevel': '2.2'
}

CUSTOM_PLATE = 'appliedbiosystems_96_wellplate_100ul'
CSV_FILE = 'SingleHeadTransfer.csv'

def run(protocol: protocol_api.ProtocolContext):

    tiprack = protocol.load_labware('geb_96_tiprack_10ul', 1)
    plate1 = protocol.load_labware(CUSTOM_PLATE, 2)
    plate2 = protocol.load_labware(CUSTOM_PLATE, 3)
    p10 = protocol.load_instrument('p10_single', mount='right', tip_racks=[tiprack])

    # for x in range(12):
    #     for y in range(8):
    #         well = chr(ord('A')+y) + str(x+1)
    #         p10.transfer(volumes[x][y], plate1[well], plate2[well])
