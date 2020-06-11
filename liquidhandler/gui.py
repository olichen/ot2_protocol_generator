import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

PIPETTE_TYPES = ('p10_single', 'p10_multi')
PIPETTE_LOCS = ('right', 'left')
TIP_RACK_TYPES = ('geb_96_tiprack_10ul', 'b')
TIP_RACK_LOCS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
PLATE_TYPES = ('appliedbiosystems_96_wellplate_100ul', 'b')
PLATE_LOCS = TIP_RACK_LOCS

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Protocol Generator')

        self.pipette_type = tk.StringVar()
        self.pipette_loc = tk.StringVar()
        self.tip_rack_type = tk.StringVar()
        self.tip_rack_loc = tk.StringVar()
        self.src_plate_type = tk.StringVar()
        self.src_plate_loc = tk.StringVar()
        self.dest_plate_type = tk.StringVar()
        self.dest_plate_loc = tk.StringVar()
        self.csv_file_loc = tk.StringVar()

        self.createGUI()

        self.window.mainloop()

    def createGUI(self):
        self.addSelectors('Pipette Type', 1, 1, self.pipette_type, PIPETTE_TYPES)
        self.addSelectors('Pipette Location', 1, 3, self.pipette_loc, PIPETTE_LOCS)

        self.addSelectors('Tip Rack Type', 2, 1, self.tip_rack_type, TIP_RACK_TYPES)
        self.addSelectors('Tip Rack Location', 2, 3, self.tip_rack_loc, TIP_RACK_LOCS)

        self.addSelectors('Source Plate Type', 3, 1, self.src_plate_type, PLATE_TYPES)
        self.addSelectors('Source Plate Location', 3, 3, self.src_plate_loc, PLATE_LOCS)

        self.addSelectors('Dest Plate Type', 4, 1, self.dest_plate_type, PLATE_TYPES)
        self.addSelectors('Dest Plate Location', 4, 3, self.dest_plate_loc, PLATE_LOCS)

        self.addCSVSelector()

        frame = ttk.Frame(self.window)
        frame.grid(row=10, column=1, columnspan=4, sticky='nesw')
        self.addSaveCancel(frame)

    def addSelectors(self, label, row, col, var, option_list):
        label = ttk.Label(self.window, text=label)
        label.config(width=16)
        label.grid(row=row, column=col, sticky='nesw')

        menu = ttk.OptionMenu(self.window, var, '', *option_list)
        menu.config(width=12)
        menu.grid(row=row, column=col+1, sticky='nesw')

    def addCSVSelector(self):
        label = ttk.Label(self.window, text='CSV File')
        label.grid(row=5, column=1, sticky='nesw')

        frame = ttk.Frame(self.window)
        frame.grid(row=5, column=2, columnspan=3, sticky='nesw')

        entry = ttk.Entry(frame, textvariable=self.csv_file_loc)
        entry.pack(fill=tk.BOTH, expand=1, side=tk.LEFT)
        csvbutton = ttk.Button(frame, text='..', width=1, command=self.getCSVFile)
        csvbutton.pack(side=tk.RIGHT)

    def addSaveCancel(self, parent):
        save = ttk.Button(parent, text='Save')
        save.grid(row=1, column=1)
        cancel = ttk.Button(parent, text='Quit', command=self.quit)
        cancel.grid(row=1, column=2)
        self.window.bind('<Escape>', self.quit)

    def getCSVFile(self):
        self.csv_file_loc.set(filedialog.askopenfilename(
            title='Select a file',
            filetypes=[('CSV Files', '*.csv')]))
        self.window.focus()

    def quit(self, event = None):
        self.window.destroy()

    def main(self):
        print('placeholder')


if __name__ == "__main__":
    GUI().main()
