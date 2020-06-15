import csv_reader
import protocol_formatter
import eight_transfer


# Class that handles receiving/validating data and outputting the protocol
class ProtocolWriter:
    def __init__(self, data):
        self.data = data
        self.csv_data = csv_reader.CSVReader(data.csv_file_loc)
        self.pf = protocol_formatter.ProtocolFormatter()

    # Outputs the protocol file
    def saveOutput(self, output_file):
        with open(output_file, 'w') as f:
            pf = protocol_formatter.ProtocolFormatter
            self.writeHeader(f)

            if self.data.pipette_type == 'single':
                self.writeSingleTransfer(f)
            elif self.data.pipette_type == 'multi':
                self.writeEightTransfer(f)
            else:
                err_str = 'Invalid pipette type: ' + self.data.pipette_type
                raise ValueError(err_str)

    # Writes the header to the output protocol file
    def writeHeader(self, f):
        f.write(self.pf.getHeader())
        f.write(self.pf.getTipRack(self.data.tip_rack_name, self.data.tip_rack_loc))
        f.write(self.pf.getSrcPlate(self.data.src_plate_name, self.data.src_plate_loc))
        f.write(self.pf.getDestPlate(self.data.dest_plate_name, self.data.dest_plate_loc))
        f.write(self.pf.getPipette(self.data.pipette_name, self.data.pipette_loc))

    # Writes all the transfers by well to the output protocol file
    def writeSingleTransfer(self, f):
        for well, volume in self.csv_data.volumes.items():
            f.write(self.pf.getSingleTransfer(volume, well))

    # Writes all the transfer by column to the output protocol file
    def writeEightTransfer(self, f):
        # Tries to process the data; raises an exception with invalid data
        et = eight_transfer.EightTransfer(self.csv_data.volumes)

        # Iterates and writes the transfers by column to the output protocol
        # file if it receives a non-empty column
        for i in range(12):
            vol = et.col_volumes[i]
            if vol:
                col = i + 1
                f.write(self.pf.getMultiTransfer(vol, col))
