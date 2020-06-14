import csv_reader
import protocol_formatter


class ProtocolWriter:
    def __init__(self, data):
        self.data = data
        self.csv_data = csv_reader.CSVReader(data.csv_file_loc)

    def saveOutput(self, output_file):
        pf = protocol_formatter.ProtocolFormatter()

        with open(output_file, 'w') as f:
            self.writeHeader(f)

            for well, volume in self.csv_data.volumes.items():
                f.write(pf.getSingleTransfer(volume, well))

    def writeHeader(self, f):
        pf = protocol_formatter.ProtocolFormatter()
        f.write(pf.getHeader())
        f.write(pf.getTipRack(self.data.tip_rack_name, self.data.tip_rack_loc))
        f.write(pf.getSrcPlate(self.data.src_plate_name, self.data.src_plate_loc))
        f.write(pf.getDestPlate(self.data.dest_plate_name, self.data.dest_plate_loc))
        f.write(pf.getPipette(self.data.pipette_name, self.data.pipette_loc))
