import tkinter as tk
from tkinter import ttk

PIPETTE_TYPES = ('p10_single', 'p10_multi')
PIPETTE_LOCS = ('right', 'left')
TIP_RACK_TYPES = ('geb_96_tiprack_10ul')
TIP_RACK_LOCS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11')
PLATE_TYPES = ('appliedbiosystems_96_wellplate_100ul')
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

        self.createGUI(self.window)

        self.window.mainloop()

    def createGUI(self, window):
        frame = ttk.LabelFrame(self.window, text="Pipette")
        frame.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addSelectors(frame, 'Pipette Type', 1, self.pipette_type, PIPETTE_TYPES)
        self.addSelectors(frame, 'Pipette Location', 2, self.pipette_loc, PIPETTE_LOCS)

        frame = ttk.LabelFrame(self.window, text="Tip Rack")
        frame.grid(row=2, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addSelectors(frame, 'Tip Rack Type', 1, self.tip_rack_type, TIP_RACK_TYPES)
        self.addSelectors(frame, 'Tip Rack Location', 2, self.tip_rack_loc, TIP_RACK_LOCS)

        frame = ttk.LabelFrame(self.window, text="Source Plate")
        frame.grid(row=3, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addSelectors(frame, 'Source Plate Type', 1, self.src_plate_type, PLATE_TYPES)
        self.addSelectors(frame, 'Source Plate Location', 2, self.src_plate_loc, PLATE_LOCS)

        frame = ttk.LabelFrame(self.window, text="Destination Plate")
        frame.grid(row=4, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addSelectors(frame, 'Destination Plate Type', 1, self.dest_plate_type, PLATE_TYPES)
        self.addSelectors(frame, 'Destination Plate Location', 2, self.dest_plate_loc, PLATE_LOCS)

        frame = ttk.Frame(self.window)
        frame.grid(row=5, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addSaveCancel(frame)

    def addSelectors(self, parent, label, row, variable, option_list):
        pipette_type_label = ttk.Label(parent, text=label)
        pipette_type_label.grid(row=row, column=1, sticky=tk.N + tk.E + tk.S + tk.W)

        pipette_type_menu = ttk.OptionMenu(parent, variable, option_list[0], *option_list)
        pipette_type_menu.grid(row=row, column=2, sticky=tk.N + tk.E + tk.S + tk.W)

    def addSaveCancel(self, parent):
        save = ttk.Button(parent, text='Save')
        save.grid(row=1, column=1)
        cancel = ttk.Button(parent, text='Quit')
        cancel.grid(row=1, column=2)
        print('savecancel')

    def main(self):
        print('placeholder')


if __name__ == "__main__":
    GUI().main()
