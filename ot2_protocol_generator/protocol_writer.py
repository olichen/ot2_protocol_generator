from . import format_helper
from . import eight_transfer
from . import csv_reader


# Class that handles receiving/validating data and outputting the protocol
class ProtocolWriter:
    def __init__(self):
        self.data = []
        self.csv_data = []
        self.pipette_type = ''
        self.fh = format_helper.FormatHelper()

    def addData(self, data):
        self.data.append(data)

        # Tries to process the data; raises an exception with invalid data
        if data.data_type == 'pipette':
            if data.isMulti():
                self.pipette_type = 'multi'
            else:
                self.pipette_type = 'single'
            self.csv_data.append('')
        elif data.data_type == 'plate':
            csv_data = csv_reader.CSVReader(data.csv_file_loc)

            if self.pipette_type == 'multi':
                csv_data = eight_transfer.EightTransfer(csv_data.volumes)
            self.csv_data.append(csv_data)
        else:
            raise Exception()

    # Checks whether we are trying to do a single transfer or a multi transfer
    def saveOutput(self, output_file):
        with open(output_file, 'w') as f:
            f.write(self.fh.getHeader())

            # First load up all the tip racks
            for data in self.data:
                if data.data_type == 'plate':
                    self.writeTipRackData(f, data)

            # Iterate through all the received data
            for i, data in enumerate(self.data):
                if data.data_type == 'pipette':
                    self.writePipetteData(f, data)
                elif data.data_type == 'plate':
                    self.writePlateData(f, data)
                    if self.pipette_type == 'multi':
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
        for i in range(12):
            vol = csv_data.col_volumes[i]
            if vol:
                col = i + 1
                f.write(self.fh.getMultiTransfer(vol, col))

    # Writes the header to the output protocol file
    def writePlateData(self, f, data):
        f.write(self.fh.getSrcPlate(data.src_plate_name, data.src_plate_loc))
        f.write(self.fh.getDestPlate(data.dest_plate_name, data.dest_plate_loc))

    def writeTipRackData(self, f, data):
        f.write(self.fh.getTipRack(data.tip_rack_name, data.tip_rack_loc))

    def writePipetteData(self, f, data):
        f.write(self.fh.getPipette(data.pipette_name, data.pipette_loc))
