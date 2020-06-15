import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import config


class ProtocolGUI:
    def __init__(self, parent):
        self.parent = parent
        self.row = 1
        self.col = 1
        self.csv_file_loc = None

    def addPipetteSelectors(self, pname, ploc):
        self.addSelectors('Pipette Type', pname, config.PIPETTE_TYPES)
        self.addSelectors('Pipette Location', ploc, config.PIPETTE_LOCS)

    def addTipRackSelectors(self, trname, trloc):
        self.addSelectors('Tip Rack Type', trname, config.TIP_RACK_TYPES)
        self.addSelectors('Tip Rack Location', trloc, config.TIP_RACK_LOCS)

    def addSourcePlateSelectors(self, spname, sploc):
        self.addSelectors('Source Plate Type', spname, config.PLATE_TYPES)
        self.addSelectors('Source Plate Location', sploc, config.PLATE_LOCS)

    def addDestPlateSelectors(self, dpname, dploc):
        self.addSelectors('Dest Plate Type', dpname, config.PLATE_TYPES)
        self.addSelectors('Dest Plate Location', dploc, config.PLATE_LOCS)

    def addSelectors(self, label, var, option_list):
        label = ttk.Label(self.parent, text=label)
        label.config(width=16)
        label.grid(row=self.row, column=self.col, sticky='nesw')

        menu = ttk.OptionMenu(self.parent, var, option_list[0], *option_list)
        menu.config(width=12)
        menu.grid(row=self.row, column=self.col+1, sticky='nesw')

        self.incrementGrid()

    def incrementGrid(self):
        if self.col == 3:
            self.row += 1
            self.col = 1
        else:
            self.col += 2

    def addCSVSelector(self, csv_file_loc):
        self.csv_file_loc = csv_file_loc
        label = ttk.Label(self.parent, text='CSV File')
        label.grid(row=100, column=1, sticky='nesw')

        frame = ttk.Frame(self.parent)
        frame.grid(row=100, column=2, columnspan=3, sticky='nesw')

        entry = ttk.Entry(frame, textvariable=csv_file_loc)
        entry.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        csvbutton = ttk.Button(frame, text='..', width=1, command=self.getCSV)
        csvbutton.pack(side=tk.RIGHT)

    def getCSV(self):
        self.csv_file_loc.set(filedialog.askopenfilename(
            title='Select a file',
            filetypes=[('CSV Files', '*.csv')]))
        self.parent.focus()
