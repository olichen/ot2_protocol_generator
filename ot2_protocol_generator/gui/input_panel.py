from tkinter import ttk
from . import config


# Creates an input panel for a transfer
class InputPanel(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.cfg = config.Configuration('./labware.ini')

    # Creates a label and a dropdown menu for the given label, variable, and
    # list of options
    def addMenu(self, label, var, option_list, row, col):
        label = ttk.Label(self, text=label)
        label.config(width=20)
        label.grid(row=row, column=col, sticky='nesw')

        menu = ttk.OptionMenu(self, var, option_list[0], *option_list)
        menu.config(width=16)
        menu.grid(row=row, column=col+1, sticky='nesw')
