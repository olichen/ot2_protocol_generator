import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from . import config
from . import protocol_data


# Creates an input panel for a transfer
class InputPanel:
    def __init__(self, parent):
        self.parent = parent
        self.row = 1
        self.col = 1

        self.tip_rack_name = tk.StringVar()
        self.tip_rack_loc = tk.StringVar()
        self.src_plate_name = tk.StringVar()
        self.src_plate_loc = tk.StringVar()
        self.dest_plate_name = tk.StringVar()
        self.dest_plate_loc = tk.StringVar()
        self.pipette_name = tk.StringVar()
        self.pipette_loc = tk.StringVar()
        self.csv_file_loc = tk.StringVar()

        self.createPipetteSelectors(self.pipette_name, self.pipette_loc)
        self.createTipRackSelectors(self.tip_rack_name, self.tip_rack_loc)
        self.createSourcePlateSelectors(self.src_plate_name, self.src_plate_loc)
        self.createDestPlateSelectors(self.dest_plate_name, self.dest_plate_loc)
        self.createCSVSelector(self.csv_file_loc)

    def getProtocolData(self):
        ptype = self.getPipetteType(self.pipette_name.get())
        return protocol_data.ProtocolData(
                tip_rack_name=self.tip_rack_name.get(),
                tip_rack_loc=self.tip_rack_loc.get(),
                src_plate_name=self.src_plate_name.get(),
                src_plate_loc=self.src_plate_loc.get(),
                dest_plate_name=self.dest_plate_name.get(),
                dest_plate_loc=self.dest_plate_loc.get(),
                pipette_name=self.pipette_name.get(),
                pipette_loc=self.pipette_loc.get(),
                pipette_type=ptype,
                csv_file_loc=self.csv_file_loc.get())

    def getPipetteType(self, pname):
        if 'single' in pname:
            return 'single'
        elif 'multi' in pname:
            return 'multi'
        else:
            err_str = "Invalid pipette: '{0}'".format(pname)
            raise ValueError(err_str)

    # Creates the selectors for the pipette
    def createPipetteSelectors(self, pname, ploc):
        self.createSelectors('Pipette Type', pname, config.PIPETTE_NAMES)
        self.createSelectors('Pipette Location', ploc, config.PIPETTE_LOCS)

    # Creates the selectors for the tip rack
    def createTipRackSelectors(self, trname, trloc):
        self.createSelectors('Tip Rack Type', trname, config.TIP_RACK_NAMES)
        self.createSelectors('Tip Rack Location', trloc, config.TIP_RACK_LOCS)

    # Creates the selectors for the source plate
    def createSourcePlateSelectors(self, spname, sploc):
        self.createSelectors('Source Plate Type', spname, config.PLATE_NAMES)
        self.createSelectors('Source Plate Location', sploc, config.PLATE_LOCS)

    # Creates the selectors for the destination plate
    def createDestPlateSelectors(self, dpname, dploc):
        self.createSelectors('Dest Plate Type', dpname, config.PLATE_NAMES)
        self.createSelectors('Dest Plate Location', dploc, config.PLATE_LOCS)

    # Creates a label and a dropdown menu for the given label, variable, and
    # list of options
    def createSelectors(self, label, var, option_list):
        label = ttk.Label(self.parent, text=label)
        label.config(width=16)
        label.grid(row=self.row, column=self.col, sticky='nesw')

        menu = ttk.OptionMenu(self.parent, var, option_list[0], *option_list)
        menu.config(width=12)
        menu.grid(row=self.row, column=self.col+1, sticky='nesw')

        self.incrementGrid()

    # Helper function that increments the grid for the GUI elements so that
    # they are aligned properly
    def incrementGrid(self):
        if self.col == 3:
            self.row += 1
            self.col = 1
        else:
            self.col += 2

    # Creates a label, text box, and button for selecting the CSV file
    def createCSVSelector(self, csv_file_loc):
        self.csv_file_loc = csv_file_loc
        label = ttk.Label(self.parent, text='CSV File')
        label.grid(row=100, column=1, sticky='nesw')

        frame = ttk.Frame(self.parent)
        frame.grid(row=100, column=2, columnspan=3, sticky='nesw')

        entry = ttk.Entry(frame, textvariable=csv_file_loc)
        entry.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        csvbutton = ttk.Button(frame, text='..', width=1, command=self.getCSV)
        csvbutton.pack(side=tk.RIGHT)

    # Pops out a file dialog for the user to select a CSV input file
    def getCSV(self):
        self.csv_file_loc.set(filedialog.askopenfilename(
            title='Select a file',
            filetypes=[('CSV Files', '*.csv')]))
        self.parent.focus()
