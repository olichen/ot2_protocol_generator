# Formats the output code for the protocol
class ProtocolFormatter:
    # Returns the code for the header
    def getHeader(self):
        return (
            "from opentrons import protocol_api\n"
            "\n"
            "metadata = {\n"
            "    'protocolName': 'OT Transfer',\n"
            "    'author': 'Oliver Chen <olichen@ucdavis.edu>',\n"
            "    'apiLevel': '2.2'\n"
            "}\n\n"
            "def run(protocol: protocol_api.ProtocolContext):\n"
            )

    # Returns the code to load a tip rack
    def getTipRack(self, rack_name, rack_location):
        return self.getLabware('tip_rack', rack_name, rack_location)

    # Returns the code to load a plate
    def getSrcPlate(self, plate_name, plate_location):
        return self.getLabware('src_plate', plate_name, plate_location)

    # Returns the code to load a plate
    def getDestPlate(self, plate_name, plate_location):
        return self.getLabware('dest_plate', plate_name, plate_location)

    # Returns the code to load a piece of labware (tip rack, plate, etc)
    def getLabware(self, var_name, labware_name, labware_location):
        return "    {0} = protocol.load_labware('{1}', {2})\n" \
            .format(var_name, labware_name, labware_location)

    # Returns the code to load a pipette
    def getPipette(self, pipette_name, pipette_location):
        return "    pipette = protocol.load_instrument(" \
            "'{0}', mount = '{1}', tip_racks = [{2}])\n\n" \
            .format(pipette_name, pipette_location, 'tip_rack')

    # Returns the code to transfer volume from a single well of the source
    # plate to the destination plate.
    def getSingleTransfer(self, volume, well):
        return "    pipette.transfer(" \
            "{0}, src_plate['{1}'], dest_plate['{1}'])\n" \
            .format(volume, well)

    # Returns the code to transfer volume from a column of wells from the
    # source plate to the destination plate using a multi-headed pipette.
    def getMultiTransfer(self, volume, column):
        return "    pipette.transfer({0}, " \
            "src_plate.columns_by_name()['{1}'], " \
            "dest_plate.columns_by_name()['{1}'])\n" \
            .format(volume, column)
