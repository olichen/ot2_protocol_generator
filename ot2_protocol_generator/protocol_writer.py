from .helpers import format_helper
from .helpers import multi_transfer_helper as mth
from .helpers import csv_helper


# Class that handles receiving/validating data and outputting the protocol
class ProtocolWriter:
    def __init__(self):
        self.data = []
        self.csv_data = []
        self.pipette_type = ''
        self.fh = format_helper.FormatHelper()

    # Add another source of data (either pipette or plate data)
    def addData(self, data):
        self.data.append(data)

        # Tries to process the data; raises an exception with invalid data
        if data.data_type == 'pipette':
            self.addPipetteData(data)
        elif data.data_type == 'plate':
            self.addPlateData(data)
        else:
            err_str = "Invalid data type. We shouldn't get here"
            raise Exception(err_str)

    # Updates the pipette type and appends an empty string to csv_data
    def addPipetteData(self, data):
        if data.isMulti():
            self.pipette_type = 'multi'
        else:
            self.pipette_type = 'single'
        self.csv_data.append('')

    # Processes and appends the CSV data
    def addPlateData(self, data):
        # Read in the csv data
        csv_data = csv_helper.CSVReader(data.csv_file_loc)

        # Pre-process the multi-head transfer data
        if self.pipette_type == 'single':
            pass
        elif self.pipette_type == 'multi':
            csv_data = mth.MultiTransferHelper(csv_data.volumes)
        else:
            err_str = "Invalid pipette type. We shouldn't ever get here"
            raise Exception(err_str)
        self.csv_data.append(csv_data)

    # Checks whether we are trying to do a single transfer or a multi transfer
    def saveOutput(self, output_file):
        with open(output_file, 'w') as f:
            # Write the header to the output file
            f.write(self.fh.getHeader())

            # Write all the tip racks to the output file for the pipettes
            self.outputTipRacks(f)

            # Write the pipette data to the output file
            self.outputPipetteData(f)

            # Iterate through all the received data
            self.outputTransferData(f)

    # Iterate through all the input data and write the tip rack definitions
    def outputTipRacks(self, f):
        for data in self.data:
            if data.data_type == 'plate':
                name = data.tip_rack_name
                loc = data.tip_rack_loc
                f.write(self.fh.getTipRack(name, loc))

    # Iterate through all the input data and write the pipette definition
    def outputPipetteData(self, f):
        for data in self.data:
            if data.data_type == 'pipette':
                name = data.pipette_name
                loc = data.pipette_loc
                f.write(self.fh.getPipette(name, loc))

    # Iterate through all the input data and write the plate definitions
    # followed by all the transfers
    def outputTransferData(self, f):
        for i, data in enumerate(self.data):
            if data.data_type == 'plate':
                # Write the plate definitions
                name = data.src_plate_name
                loc = data.src_plate_loc
                f.write(self.fh.getSrcPlate(name, loc))
                name = data.dest_plate_name
                loc = data.dest_plate_loc
                f.write(self.fh.getDestPlate(name, loc))

                # Write transfers
                if self.pipette_type == 'multi':
                    self.outputMultiTransfers(f, self.csv_data[i])
                elif self.pipette_type == 'single':
                    self.outputSingleTransfers(f, self.csv_data[i])
                else:
                    err_str = "Invalid pipette type. We shouldn't get here"
                    raise Exception(err_str)

    # Writes all the transfers by well to the output protocol file
    def outputSingleTransfers(self, f, csv_data):
        for well, volume in csv_data.volumes.items():
            f.write(self.fh.getSingleTransfer(volume, well))

    # Writes all the transfer by column to the output protocol file
    def outputMultiTransfers(self, f, csv_data):
        # Iterates and writes the transfers by column to the output protocol
        # file if it receives a non-empty column
        for i in range(12):
            vol = csv_data.col_volumes[i]
            if vol:
                col = i + 1
                f.write(self.fh.getMultiTransfer(vol, col))
