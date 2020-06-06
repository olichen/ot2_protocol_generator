import os
import tkinter as tk
from tkinter import filedialog
import csv_reader

# class ProtocolGenerator:
#     def __init__(self, transfer_type, csv_file, protocol_file):
#         self.transfer_type = transfer_type
#         self.csv_file = csv_file
#         self.tip_rack_loc = 1
#         self.tip_rack_type = 'geb_96_tiprack_10ul'
#         self.src_plate_loc = 2
#         self.src_plate_type = 'appliedbiosystems_96_wellplate_100ul'
#         self.dest_plate_loc = 3
#         self.dest_plate_type = 'appliedbiosystems_96_wellplate_100ul'

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title = 'Select a file', filetypes = [('csv files','*.csv')])
print(file_path)


