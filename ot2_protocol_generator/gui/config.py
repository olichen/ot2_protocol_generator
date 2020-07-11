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
            value = 'p10_single,p10_multi'
            self.config.set('LABWARE', 'PIPETTE_NAMES', value)
        if not self.config.has_option('LABWARE', 'PIPETTE_LOCS'):
            value = 'right,left'
            self.config.set('LABWARE', 'PIPETTE_LOCS', value)

    # Overload the ['getitem'] operator
    def __getitem__(self, index):
        labware = self.config['LABWARE']
        return [s.strip() for s in labware.get(index).split(',')]

    # Write the ini file
    def writeFile(self, filename):
        with open(filename, 'w') as configfile:
            self.config.write(configfile)
