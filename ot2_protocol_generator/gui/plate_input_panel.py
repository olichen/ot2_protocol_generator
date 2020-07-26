import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from .input_panel import InputPanel
from . import plate_data


# Creates an input panel for a transfer
class PlateInputPanel(InputPanel):
    def __init__(self, parent):
        super(PlateInputPanel, self).__init__(parent)

        self.tip_rack_name = tk.StringVar()
        self.tip_rack_loc = tk.StringVar()
        self.src_plate_name = tk.StringVar()
        self.src_plate_loc = tk.StringVar()
        self.dest_plate_name = tk.StringVar()
        self.dest_plate_loc = tk.StringVar()
        self.csv_file_loc = tk.StringVar()

        self.addInputPanels()

    def getData(self):
        return plate_data.PlateData(
                tip_rack_name=self.tip_rack_name.get(),
                tip_rack_loc=self.tip_rack_loc.get(),
                src_plate_name=self.src_plate_name.get(),
                src_plate_loc=self.src_plate_loc.get(),
                dest_plate_name=self.dest_plate_name.get(),
                dest_plate_loc=self.dest_plate_loc.get(),
                csv_file_loc=self.csv_file_loc.get())

    def addInputPanels(self):
        self.addTipRackMenu(self.tip_rack_name, self.tip_rack_loc)
        self.addSourcePlateMenu(self.src_plate_name, self.src_plate_loc)
        self.addDestPlateMenu(self.dest_plate_name, self.dest_plate_loc)
        self.addCSVMenu(self.csv_file_loc)

    # Creates the selectors for the tip rack
    def addTipRackMenu(self, name, loc):
        self.addMenu('Tip Rack Type', name, self.cfg['TIP_RACK_NAMES'], 1, 1)
        self.addMenu('Tip Rack Location', loc, self.cfg['TIP_RACK_LOCS'], 1, 3)

    # Creates the selectors for the source plate
    def addSourcePlateMenu(self, name, loc):
        self.addMenu('Source Plate Type', name, self.cfg['PLATE_NAMES'], 2, 1)
        self.addMenu('Source Plate Location', loc, self.cfg['PLATE_LOCS'], 2, 3)

    # Creates the selectors for the destination plate
    def addDestPlateMenu(self, name, loc):
        self.addMenu('Dest Plate Type', name, self.cfg['PLATE_NAMES'], 3, 1)
        self.addMenu('Dest Plate Location', loc, self.cfg['PLATE_LOCS'], 3, 3)

    # Creates a label, text box, and button for selecting the CSV file
    def addCSVMenu(self, csv_file_loc):
        self.csv_file_loc = csv_file_loc
        label = ttk.Label(self, text='CSV File')
        label.grid(row=4, column=1, sticky='nesw')

        frame = ttk.Frame(self)
        frame.grid(row=4, column=2, columnspan=3, sticky='nesw')

        entry = ttk.Entry(frame, textvariable=csv_file_loc)
        entry.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        csvbutton = ttk.Button(frame, text='..', width=2, command=self.getCSV)
        csvbutton.pack(side=tk.RIGHT)

    # Pops out a file dialog for the user to select a CSV input file
    def getCSV(self):
        csv_file = filedialog.askopenfilename(
            title='Select a file',
            filetypes=[('CSV Files', '*.csv')])
        if csv_file:
            self.csv_file_loc.set(csv_file)
        self.focus()
