from . import format_helper
from . import eight_transfer


# Class that handles receiving/validating data and outputting the protocol
class ProtocolWriter:
    def __init__(self):
        self.protocol_data = []
        self.csv_data = []
        self.fh = format_helper.FormatHelper()


    def addInput(self, protocol_data, csv_data):
        self.protocol_data.append(protocol_data)

        # Tries to process the data; raises an exception with invalid data
        if protocol_data.isMulti():
            csv_data = eight_transfer.EightTransfer(csv_data.volumes)
        self.csv_data.append(csv_data)


    # Checks whether we are trying to do a single transfer or a multi transfer
    def saveOutput(self, output_file):
        with open(output_file, 'w') as f:
            f.write(self.fh.getHeader())

            # Iterate through all the received data
            for i in range(len(self.protocol_data)):
                self.writeProtocolData(f, self.protocol_data[i])

                if self.protocol_data[i].isMulti():
                    self.writeEightTransfer(f, self.csv_data[i])
                else:
                    self.writeSingleTransfer(f, self.csv_data[i])

    # Writes all the transfers by well to the output protocol file
    def writeSingleTransfer(self, f, csv_data):
        for well, volume in csv_data.volumes.items():
            f.write(self.fh.getSingleTransfer(volume, well))

    # Writes all the transfer by column to the output protocol file
    def writeEightTransfer(self, f, csv_data):
        # Iterates and writes the transfers by column to the output protocol
        # file if it receives a non-empty column
        for vol in csv_data.col_volumes:
            if vol:
                col = i + 1
                f.write(self.fh.getMultiTransfer(vol, col))

    # Writes the header to the output protocol file
    def writeProtocolData(self, f, data):
        f.write(self.fh.getTipRack(data.tip_rack_name, data.tip_rack_loc))
        f.write(self.fh.getSrcPlate(data.src_plate_name, data.src_plate_loc))
        f.write(self.fh.getDestPlate(data.dest_plate_name, data.dest_plate_loc))
        f.write(self.fh.getPipette(data.pipette_name, data.pipette_loc))
