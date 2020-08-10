# Formats the output code for the protocol
class FormatHelper:
    # Returns the code for the header
    def header(self):
        return ("from opentrons import protocol_api\n\n"
                "metadata = {\n"
                "    'apiLevel': '2.2'\n"
                "}\n\n\n"
                "def run(protocol: protocol_api.ProtocolContext):\n"
                "    tip_racks = []\n")

    # Returns the code to load a tip rack
    def tipRack(self, rack_name, rack_location):
        msg = self.labware('tip_rack', rack_name, rack_location)
        msg += "    tip_racks.append(tip_rack)\n"
        return msg

    # Returns the code to load a plate
    def srcPlate(self, plate_name, plate_location):
        return self.labware('src_plate', plate_name, plate_location)

    # Returns the code to load a plate
    def destPlate(self, plate_name, plate_location):
        return self.labware('dest_plate', plate_name, plate_location)

    # Returns the code to load a piece of labware (tip rack, plate, etc)
    def labware(self, var_name, lw_name, lw_loc):
        return (f"    {var_name} = protocol.load_labware("
                f"'{lw_name}', {lw_loc})\n")

    # Returns the code to load a pipette
    def pipette(self, p_name, p_loc):
        return ("    pipette = protocol.load_instrument("
                f"'{p_name}', mount='{p_loc}', tip_racks=tip_racks)\n\n")

    # Returns the code to transfer volume from a single well of the source
    # plate to the destination plate.
    def singleTransfer(self, vol, well):
        return ("    pipette.transfer("
                f"{vol}, src_plate['{well}'], dest_plate['{well}'])\n")

    # Returns the code to transfer volume from a column of wells from the
    # source plate to the destination plate using a multi-headed pipette.
    def multiTransfer(self, vol, col):
        return (f"    pipette.transfer({vol}, "
                f"src_plate.columns_by_name()['{col}'], "
                f"dest_plate.columns_by_name()['{col}'])\n")

    # Returns the code to transfer volume from well to well, with blowout
    def transfer(self, vol, well):
        msg = "    pipette.pick_up_tip()\n"
        while vol > 0:
            xfer = min(10.0, vol)
            msg += (f"    pipette.aspirate({xfer}, src_plate.wells()[{well}]"
                    f".bottom())\n")
            msg += (f"    pipette.dispense({xfer}, dest_plate.wells()[{well}])"
                    f".blow_out(dest_plate.wells()[{well}])\n")
            vol -= xfer
        msg += f"    pipette.drop_tip()\n"
        return msg
