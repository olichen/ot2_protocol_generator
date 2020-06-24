import tkinter as tk
from . import config
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

        self.createInputPanels()

    def getProtocolData(self):
        return plate_data.PlateData(
                tip_rack_name=self.tip_rack_name.get(),
                tip_rack_loc=self.tip_rack_loc.get(),
                src_plate_name=self.src_plate_name.get(),
                src_plate_loc=self.src_plate_loc.get(),
                dest_plate_name=self.dest_plate_name.get(),
                dest_plate_loc=self.dest_plate_loc.get(),
                csv_file_loc=self.csv_file_loc.get())

    def createInputPanels(self):
        self.createTipRackSelectors(self.tip_rack_name, self.tip_rack_loc)
        self.createSourcePlateSelectors(self.src_plate_name, self.src_plate_loc)
        self.createDestPlateSelectors(self.dest_plate_name, self.dest_plate_loc)
        self.createCSVSelector(self.csv_file_loc)

    # Creates the selectors for the tip rack
    def createTipRackSelectors(self, trname, trloc):
        self.createSelectors('Tip Rack Type', trname, config.TIP_RACK_NAMES, 1, 1)
        self.createSelectors('Tip Rack Location', trloc, config.TIP_RACK_LOCS, 1, 3)

    # Creates the selectors for the source plate
    def createSourcePlateSelectors(self, spname, sploc):
        self.createSelectors('Source Plate Type', spname, config.PLATE_NAMES, 2, 1)
        self.createSelectors('Source Plate Location', sploc, config.PLATE_LOCS, 2, 3)

    # Creates the selectors for the destination plate
    def createDestPlateSelectors(self, dpname, dploc):
        self.createSelectors('Dest Plate Type', dpname, config.PLATE_NAMES, 3, 1)
        self.createSelectors('Dest Plate Location', dploc, config.PLATE_LOCS, 3, 3)
