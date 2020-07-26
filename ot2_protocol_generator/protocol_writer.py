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
            f.write(self.fh.header())
            self.outputTipRacks(f)
            self.outputPipetteData(f)
            self.outputTransferData(f)

    # Iterate through all the input data and write the tip rack definitions
    def outputTipRacks(self, f):
        for d in self.plate_data:
            f.write(self.fh.tipRack(d.tip_rack_name, d.tip_rack_loc))

    # Write the pipette definition
    def outputPipetteData(self, f):
        d = self.pipette_data
        f.write(self.fh.pipette(d.pipette_name, d.pipette_loc))

    # Iterate through all the input data and write the plate definitions
    # followed by all the transfers
    def outputTransferData(self, f):
        for d, csv in zip(self.plate_data, self.plate_csv):
            f.write(self.fh.srcPlate(d.src_plate_name, d.src_plate_loc))
            f.write(self.fh.destPlate(d.dest_plate_name, d.dest_plate_loc))

            if self.pipette_data.isMulti():
                for i, vol in enumerate(csv.col_volumes):
                    if vol:
                        f.write(self.fh.multiTransfer(vol, i+1))
            else:
                for well, vol in csv.volumes.items():
                    f.write(self.fh.singleTransfer(vol, well))
