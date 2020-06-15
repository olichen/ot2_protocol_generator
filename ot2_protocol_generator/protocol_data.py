from dataclasses import dataclass


# Dataclass to hold the data that defines the protocol
@dataclass
class ProtocolData:
    tip_rack_name: str
    tip_rack_loc: str
    src_plate_name: str
    src_plate_loc: str
    dest_plate_name: str
    dest_plate_loc: str
    pipette_name: str
    pipette_type: str
    pipette_loc: str
    csv_file_loc: str

    # Check to make sure the inputted data is valid
    # Raises an exception if the data is invalid
    def isValid(self):
        self.checkMissingInput()
        self.checkPlateLocations()

        return True

    # Check to make sure there is are no missing fields
    # Raises an exception on missing fields
    def checkMissingInput(self):
        missing_input = []
        for key, value in self.__dict__.items():
            if not value:
                missing_input.append(key)

        if missing_input:
            err_str = 'Missing input for:'
            for value in missing_input:
                err_str += ' '
                err_str += value
            raise ValueError(err_str)

    # Check to make sure that plate locations are not shared
    # Raises an exception if plate locations are shared
    def checkPlateLocations(self):
        if self.tip_rack_loc == self.src_plate_loc:
            err_str = 'Tip rack and source plate are in the same location'
            raise ValueError(err_str)
        if self.tip_rack_loc == self.dest_plate_loc:
            err_str = 'Tip rack and destination plate are in the same location'
            raise ValueError(err_str)
        if self.src_plate_loc == self.dest_plate_loc:
            err_str = 'Source and destination plate are in the same location'
            raise ValueError(err_str)
