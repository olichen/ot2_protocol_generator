import os
import tkinter as tk
from tkinter import filedialog
import csv_reader


class ProtocolGenerator:
    def __init__(self):
        self.csv_file = 'placeholder'
        self.tip_rack_loc = 1
        self.tip_rack_type = 'geb_96_tiprack_10ul'
        self.src_plate_loc = 2
        self.src_plate_type = 'appliedbiosystems_96_wellplate_100ul'
        self.dest_plate_loc = 3
        self.dest_plate_type = 'appliedbiosystems_96_wellplate_100ul'
        self.pipette = 'p10_single'
        self.pipette_location = 'right'

    def main(self):
        file_path = self.getCSVFile()
        csvr = csv_reader.CSVReader(file_path)
        print(csvr.volumes)
        file_path = self.getOutputFile()
        self.saveOutput(file_path, csvr.volumes.items())


    def saveOutput(self, output_file, csv_volumes):
        with open(output_file, 'w') as f1:
            with open('single_head_transfer.py') as f:
                for line in f:
                    f1.write(line)
            for well, volume in csv_volumes:
                f1.write('    p10.transfer(' + volume + ", plate1['" + well + "'], plate2['" + well + "'])\n")


    def getCSVFile(self):
        root = tk.Tk()
        root.withdraw()
        return filedialog.askopenfilename(
                title = 'Select a file',
                filetypes = [('CSV Files','*.csv')])

    def getOutputFile(self):
        root = tk.Tk()
        root.withdraw()
        files = [('Python Files', '*.py')]
        return filedialog.asksaveasfilename(
                title = 'Save output file',
                filetypes = files)

if __name__ == "__main__":
    ProtocolGenerator().main()
