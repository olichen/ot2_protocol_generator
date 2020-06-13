import csv_reader
import protocol_formatter


class ProtocolWriter:
    def __init__(self, data):
        self.data = data
        self.csv_data = csv_reader.CSVReader(data.csv_file_loc)

    def saveOutput(self, output_file):
        pf = protocol_formatter.ProtocolFormatter()

        with open(output_file, 'w') as f1:
            f1.write(pf.getHeader())
            f1.write(pf.getTipRack(self.data.tip_rack_type, self.data.tip_rack_loc))
            f1.write(pf.getSrcPlate(self.data.src_plate_type, self.data.src_plate_loc))
            f1.write(pf.getDestPlate(self.data.dest_plate_type, self.data.dest_plate_loc))
            f1.write(pf.getPipette(self.data.pipette_type, self.data.pipette_loc))

            for well, volume in self.csv_data.volumes.items():
                f1.write(pf.getSingleTransfer(volume, well))
