import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


# Creates an input panel for a transfer
class InputPanel:
    def __init__(self, parent):
        self.parent = parent

    # Creates a label and a dropdown menu for the given label, variable, and
    # list of options
    def createSelectors(self, label, var, option_list, row, col):
        label = ttk.Label(self.parent, text=label)
        label.config(width=16)
        label.grid(row=row, column=col, sticky='nesw')

        menu = ttk.OptionMenu(self.parent, var, option_list[0], *option_list)
        menu.config(width=12)
        menu.grid(row=row, column=col+1, sticky='nesw')

    # Creates a label, text box, and button for selecting the CSV file
    def createCSVSelector(self, csv_file_loc):
        self.csv_file_loc = csv_file_loc
        label = ttk.Label(self.parent, text='CSV File')
        label.grid(row=4, column=1, sticky='nesw')

        frame = ttk.Frame(self.parent)
        frame.grid(row=4, column=2, columnspan=3, sticky='nesw')

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
