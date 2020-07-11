import tkinter as tk
from .input_panel import InputPanel
from . import pipette_data


# Creates an input panel for a transfer
class PipetteInputPanel(InputPanel):
    def __init__(self, parent):
        super(PipetteInputPanel, self).__init__(parent)

        self.pipette_name = tk.StringVar()
        self.pipette_loc = tk.StringVar()

        self.createPipetteMenu(self.pipette_name, self.pipette_loc)

    def getData(self):
        return pipette_data.PipetteData(
                pipette_name=self.pipette_name.get(),
                pipette_loc=self.pipette_loc.get())

    # Creates the selectors for the pipette
    def createPipetteMenu(self, pname, ploc):
        self.addMenu('Pipette Type', pname, self.cfg.PIPETTE_NAMES, 1, 1)
        self.addMenu('Pipette Location', ploc, self.cfg.PIPETTE_LOCS, 1, 3)
