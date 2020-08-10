from .helpers import format_helper
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

            # Add csv data. Validate multi-head transfer data
            csv_data = csv_helper.CSVReader(data.csv_file_loc)
            if self.pipette_data.isMulti():
                csv_data.validate_multi_transfer()
            self.plate_csv.append(csv_data.volumes)

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
            f.write(self.fh.tip_rack(d.tip_rack_name, d.tip_rack_loc))

    # Write the pipette definition
    def outputPipetteData(self, f):
        d = self.pipette_data
        f.write(self.fh.pipette(d.pipette_name, d.pipette_loc))

    # Iterate through all the input data and write the plate definitions
    # followed by all the transfers
    def outputTransferData(self, f):
        for d, csv in zip(self.plate_data, self.plate_csv):
            f.write(self.fh.src_plate(d.src_plate_name, d.src_plate_loc))
            f.write(self.fh.dest_plate(d.dest_plate_name, d.dest_plate_loc))

            if self.pipette_data.isMulti():
                for i in range(0,96,8):
                    f.write(self.fh.transfer(csv[i], i))
            else:
                for i, vol in enumerate(csv):
                    f.write(self.fh.transfer(vol, i))
