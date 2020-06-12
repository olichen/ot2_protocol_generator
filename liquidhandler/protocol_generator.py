import tkinter as tk
from tkinter import filedialog
import csv_reader
import protocol_formatter
import protocol_data


class ProtocolGenerator:
    def __init__(self, output_file, data):
        csvr = csv_reader.CSVReader(data.csv_file_loc)
        self.saveOutput(output_file, data, csvr.volumes.items())

    def saveOutput(self, output_file, data, csv_volumes):
        pf = protocol_formatter.ProtocolFormatter()

        with open(output_file, 'w') as f1:
            f1.write(pf.getHeader())
            f1.write(pf.getTipRack(data.tip_rack_type, data.tip_rack_loc))
            f1.write(pf.getSrcPlate(data.src_plate_type, data.src_plate_loc))
            f1.write(pf.getDestPlate(data.dest_plate_type, data.dest_plate_loc))
            f1.write(pf.getPipette(data.pipette_type, data.pipette_loc))

            for well, volume in csv_volumes:
                f1.write(pf.getSingleTransfer(volume, well))
