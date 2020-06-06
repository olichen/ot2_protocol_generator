import os
import tkinter as tk
from tkinter import filedialog
import csv_reader

# class ProtocolGenerator:
#     def __init__(self, transfer_type, csv_file, protocol_file):
#         self.transfer_type = transfer_type

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
        title = 'Select a file', filetypes = [('csv files','*.csv')])
print(file_path)

csvr = csv_reader.CSVReader(file_path)
print(csvr.volumes)

csv_file = file_path
tip_rack_loc = 1
tip_rack_type = 'geb_96_tiprack_10ul'
src_plate_loc = 2
src_plate_type = 'appliedbiosystems_96_wellplate_100ul'
dest_plate_loc = 3
dest_plate_type = 'appliedbiosystems_96_wellplate_100ul'
pipette = 'p10_single'
pipette_location = 'right'

with open("out.py", "w") as f1:
    with open("single_head_transfer.py") as f:
        for line in f:
            f1.write(line)
    for well, volume in csvr.volumes.items():
        f1.write('    p10.transfer(' + volume + ", plate1['" + well + "'], plate2['" + well + "'])\n")

