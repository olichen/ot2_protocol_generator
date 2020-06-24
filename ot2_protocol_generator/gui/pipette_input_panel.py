import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from . import config
from . import gui_helper
from . import pipette_data


# Creates an input panel for a transfer
class PipetteInputPanel:
    def __init__(self, parent):
        self.gh = gui_helper.GUIHelper(parent)

        self.pipette_name = tk.StringVar()
        self.pipette_loc = tk.StringVar()

        self.createPipetteSelectors(self.pipette_name, self.pipette_loc)

    def getData(self):
        return pipette_data.PipetteData(
                pipette_name=self.pipette_name.get(),
                pipette_loc=self.pipette_loc.get())

    # Creates the selectors for the pipette
    def createPipetteSelectors(self, pname, ploc):
        self.gh.createSelectors('Pipette Type', pname, config.PIPETTE_NAMES, 1, 1)
        self.gh.createSelectors('Pipette Location', ploc, config.PIPETTE_LOCS, 1, 3)
