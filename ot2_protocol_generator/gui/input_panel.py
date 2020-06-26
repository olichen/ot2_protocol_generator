from tkinter import ttk


# Creates an input panel for a transfer
class InputPanel:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)

    # Creates a label and a dropdown menu for the given label, variable, and
    # list of options
    def addMenu(self, label, var, option_list, row, col):
        label = ttk.Label(self.frame, text=label)
        label.config(width=16)
        label.grid(row=row, column=col, sticky='nesw')

        menu = ttk.OptionMenu(self.frame, var, option_list[0], *option_list)
        menu.config(width=12)
        menu.grid(row=row, column=col+1, sticky='nesw')

    def destroy(self):
        self.frame.destroy()
