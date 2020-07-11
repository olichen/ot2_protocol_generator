from configparser import ConfigParser


class Configuration:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read('labware.ini')

        fb_trn = 'geb_96_tiprack_10ul'
        fb_trl = '1,2,3,4,5,6,7,8,9,10,11'
        fb_pln = 'appliedbiosystems_96_wellplate_100ul'
        fb_pll = '1,2,3,4,5,6,7,8,9,10,11'
        fb_pin = 'p10_single,p10_multi'
        fb_pil = 'right,left'

        self.TIP_RACK_NAMES = self.getConfig('TIP_RACK_NAMES', fb_trn)
        self.TIP_RACK_LOCS = self.getConfig('TIP_RACK_LOCS', fb_trl)
        self.PLATE_NAMES = self.getConfig('PLATE_NAMES', fb_pln)
        self.PLATE_LOCS = self.getConfig('PLATE_LOCS', fb_pll)
        self.PIPETTE_NAMES = self.getConfig('PIPETTE_NAMES', fb_pin)
        self.PIPETTE_LOCS = self.getConfig('PIPETTE_LOCS', fb_pil)

    def getConfig(self, name, fallback):
        if 'LABWARE' in self.config:
            labware = self.config['LABWARE']
            return [s.strip() for s in labware.get(name, fallback).split(',')]
        else:
            return [s.strip() for s in fallback.split(',')]
