from tkinter import ttk


# Creates an input panel for a transfer
class InputPanel:
    def __init__(self, parent):
        self.parent = parent

    # Creates a label and a dropdown menu for the given label, variable, and
    # list of options
    def addMenu(self, label, var, option_list, row, col):
        label = ttk.Label(self.parent, text=label)
        label.config(width=16)
        label.grid(row=row, column=col, sticky='nesw')

        menu = ttk.OptionMenu(self.parent, var, option_list[0], *option_list)
        menu.config(width=12)
        menu.grid(row=row, column=col+1, sticky='nesw')
