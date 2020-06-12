import tkinter as tk
from tkinter import filedialog
import csv_reader
import output_writer
import protocol_data


class ProtocolGenerator:
    def __init__(self, output_file, data):
        csvr = csv_reader.CSVReader(data.csv_file_loc)
        self.saveOutput(output_file, data, csvr.volumes.items())

    def saveOutput(self, output_file, data, csv_volumes):
        ow = output_writer.OutputWriter()

        with open(output_file, 'w') as f1:
            f1.write(ow.getHeader())
            f1.write(ow.getTipRack(data.tip_rack_type, data.tip_rack_loc))
            f1.write(ow.getSrcPlate(data.src_plate_type, data.src_plate_loc))
            f1.write(ow.getDestPlate(data.dest_plate_type, data.dest_plate_loc))
            f1.write(ow.getPipette(data.pipette_type, data.pipette_loc))

            for well, volume in csv_volumes:
                f1.write(ow.getSingleTransfer(volume, well))
