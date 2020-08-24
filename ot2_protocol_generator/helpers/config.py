from configparser import ConfigParser


# Initializes the values for the dropdown menus. Attempts to read a
# labware.ini file, and sets default values if they are not found
class Configuration:
    def __init__(self, configfile):
        self.config = ConfigParser()
        self.config.read(configfile)

        # Set default values
        if not self.config.has_section('LABWARE'):
            self.config.add_section('LABWARE')
        if not self.config.has_option('LABWARE', 'TIP_RACK_NAMES'):
            value = 'geb_96_tiprack_10ul'
            self.config.set('LABWARE', 'TIP_RACK_NAMES', value)
        if not self.config.has_option('LABWARE', 'TIP_RACK_LOCS'):
            value = '1,2,3,4,5,6,7,8,9,10,11'
            self.config.set('LABWARE', 'TIP_RACK_LOCS', value)
        if not self.config.has_option('LABWARE', 'PLATE_NAMES'):
            value = 'appliedbiosystems_96_wellplate_100ul'
            self.config.set('LABWARE', 'PLATE_NAMES', value)
        if not self.config.has_option('LABWARE', 'PLATE_LOCS'):
            value = '1,2,3,4,5,6,7,8,9,10,11'
            self.config.set('LABWARE', 'PLATE_LOCS', value)
        if not self.config.has_option('LABWARE', 'PIPETTE_NAMES'):
            value = 'p10_multi,p10_single'
            self.config.set('LABWARE', 'PIPETTE_NAMES', value)
        if not self.config.has_option('LABWARE', 'PIPETTE_LOCS'):
            value = 'left,right'
            self.config.set('LABWARE', 'PIPETTE_LOCS', value)
        if not self.config.has_section('TRANSFER'):
            self.config.add_section('TRANSFER')
        if not self.config.has_option('TRANSFER', 'ASPIRATE_OFFSET'):
            value = '0.2'
            self.config.set('TRANSFER', 'ASPIRATE_OFFSET', value)
        if not self.config.has_option('TRANSFER', 'ASPIRATE_RATE'):
            value = '0.5'
            self.config.set('TRANSFER', 'ASPIRATE_RATE', value)
        if not self.config.has_option('TRANSFER', 'AIR_GAP'):
            value = '1.0'
            self.config.set('TRANSFER', 'AIR_GAP', value)
        if not self.config.has_option('TRANSFER', 'BLOW_OUT_RATE'):
            value = '1000.0'
            self.config.set('TRANSFER', 'BLOW_OUT_RATE', value)

    # Overload the ['getitem'] operator. Returns options as a list
    def __getitem__(self, index):
        return self.get_labware(index)

    def get_labware(self, index):
        labware = self.config['LABWARE']
        return [s.strip() for s in labware.get(index).split(',')]

    def get_transfer(self, index):
        return self.config['TRANSFER'].getfloat(index)

    # Write the configuration file
    def writeFile(self, filename):
        with open(filename, 'w') as configfile:
            self.config.write(configfile)
