from configparser import ConfigParser


class Configuration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('labware.ini')
        global TIP_RACK_NAMES
        global TIP_RACK_LOCS
        global PLATE_NAMES
        global PLATE_LOCS
        global PIPETTE_NAMES
        global PIPETTE_LOCS
        TIP_RACK_NAMES = self.getConfig('TIP_RACK_NAMES', TIP_RACK_NAMES)
        TIP_RACK_LOCS = self.getConfig('TIP_RACK_LOCS', TIP_RACK_LOCS)
        PLATE_NAMES = self.getConfig('PLATE_NAMES', PLATE_NAMES)
        PLATE_LOCS = self.getConfig('PLATE_LOCS', PLATE_LOCS)
        PIPETTE_NAMES = self.getConfig('PIPETTE_NAMES', PIPETTE_NAMES)
        PIPETTE_LOCS = self.getConfig('PIPETTE_LOCS', PIPETTE_LOCS)

    def getConfig(self, name, fallback):
        if 'LABWARE' in self.config:
            labware = self.config['LABWARE']
            return [s.strip() for s in labware.get(name, fallback).split(',')]
        else:
            return [s.strip() for s in fallback.split(',')]


TIP_RACK_NAMES = 'geb_96_tiprack_10ul'
TIP_RACK_LOCS = '1,2,3,4,5,6,7,8,9,10,11'
PLATE_NAMES = 'appliedbiosystems_96_wellplate_100ul'
PLATE_LOCS = TIP_RACK_LOCS
PIPETTE_NAMES = 'p10_single,p10_multi'
PIPETTE_LOCS = 'right,left'

Configuration()
