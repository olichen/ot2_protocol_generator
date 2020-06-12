from dataclasses import dataclass


@dataclass
class ProtocolData:
    pipette_type: str
    pipette_loc: str
    tip_rack_type: str
    tip_rack_loc: str
    src_plate_type: str
    src_plate_loc: str
    dest_plate_type: str
    dest_plate_loc: str
    csv_file_loc: str
