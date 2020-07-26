from .helpers import format_helper
from .helpers import multi_transfer_helper as mth
from .helpers import csv_helper


# Class that handles receiving/validating data and outputting the protocol
class ProtocolWriter:
    def __init__(self):
        self.pipette_data = None
        self.plate_data = []
        self.plate_csv = []
        self.fh = format_helper.FormatHelper()

    # Add another source of data (either pipette or plate data)
    def addData(self, data):
        if data.data_type == 'pipette':
            self.pipette_data = data
        elif data.data_type == 'plate':
            self.plate_data.append(data)

            # Add csv data. Pre-process multi-head transfer data
            csv_data = csv_helper.CSVReader(data.csv_file_loc)
            if self.pipette_data.isMulti():
                csv_data = mth.MultiTransferHelper(csv_data.volumes)
            self.plate_csv.append(csv_data)

    # Open the output file and write everything
    def saveOutput(self, output_file):
        with open(output_file, 'w') as f:
            f.write(self.fh.getHeader())
            self.outputTipRacks(f)
            self.outputPipetteData(f)
            self.outputTransferData(f)

    # Iterate through all the input data and write the tip rack definitions
    def outputTipRacks(self, f):
        for data in self.plate_data:
            name = data.tip_rack_name
            loc = data.tip_rack_loc
            f.write(self.fh.getTipRack(name, loc))

    # Write the pipette definition
    def outputPipetteData(self, f):
        name = self.pipette_data.pipette_name
        loc = self.pipette_data.pipette_loc
        f.write(self.fh.getPipette(name, loc))

    # Iterate through all the input data and write the plate definitions
    # followed by all the transfers
    def outputTransferData(self, f):
        for data, csv in zip(self.plate_data, self.plate_csv):
            # Write the plate definitions
            name = data.src_plate_name
            loc = data.src_plate_loc
            f.write(self.fh.getSrcPlate(name, loc))
            name = data.dest_plate_name
            loc = data.dest_plate_loc
            f.write(self.fh.getDestPlate(name, loc))

            # Write transfers
            if self.pipette_data.isMulti():
                self.outputMultiTransfers(f, csv)
            else:
                self.outputSingleTransfers(f, csv)

    # Writes all the transfers by well to the output protocol file
    def outputSingleTransfers(self, f, csv_data):
        for well, volume in csv_data.volumes.items():
            f.write(self.fh.getSingleTransfer(volume, well))

    # Writes all the transfer by column to the output protocol file
    def outputMultiTransfers(self, f, csv_data):
        # Iterates and writes the transfers by column to the output protocol
        # file if it receives a non-empty column
        for i in range(12):
            if vol := csv_data.col_volumes[i]:
                f.write(self.fh.getMultiTransfer(vol, i+1))
