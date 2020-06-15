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

    # Check to make sure there is input data for every variable
    def isValid(self):
        missing_input = []
        for key, value in self.__dict__.items():
            if not value:
                missing_input.append(key)

        if missing_input:
            error_message = 'Missing input for:'
            for value in missing_input:
                error_message += ' '
                error_message += value
            raise ValueError(error_message)

        return True
