import csv_reader
import protocol_formatter


class ProtocolWriter:
    def __init__(self, data):
        self.data = data
        self.csv_data = csv_reader.CSVReader(data.csv_file_loc)
        self.pf = protocol_formatter.ProtocolFormatter()

    def saveOutput(self, output_file):

        with open(output_file, 'w') as f:
            pf = protocol_formatter.ProtocolFormatter
            self.writeHeader(f)

            if self.data.pipette_type == 'single':
                self.writeSingleTransfer(f)
            elif self.data.pipette_type == 'multi':
                self.writeMultiTransfer(f)
            else:
                raise ValueError('Invalid pipette type: ' + self.data.pipette_type)

    def writeHeader(self, f):
        f.write(self.pf.getHeader())
        f.write(self.pf.getTipRack(self.data.tip_rack_name, self.data.tip_rack_loc))
        f.write(self.pf.getSrcPlate(self.data.src_plate_name, self.data.src_plate_loc))
        f.write(self.pf.getDestPlate(self.data.dest_plate_name, self.data.dest_plate_loc))
        f.write(self.pf.getPipette(self.data.pipette_name, self.data.pipette_loc))

    def writeSingleTransfer(self, f):
        for well, volume in self.csv_data.volumes.items():
            f.write(self.pf.getSingleTransfer(volume, well))

    def writeMultiTransfer(self, f):
        for well, volume in self.csv_data.volumes.items():
            f.write(self.pf.getSingleTransfer(volume, well))
