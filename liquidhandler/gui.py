import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Protocol Generator')

        pipette_frame = ttk.LabelFrame(self.window, text="Pipette")
        pipette_frame.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addPipette(pipette_frame)
        # self.combobox_value = tk.StringVar()

        savecancel_frame = ttk.Frame(self.window)
        savecancel_frame.grid(row=2, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addSaveCancel(savecancel_frame)

        # save = tk.Button(self.window, text='Save')
        # save.grid(row=1, column=2)
        # cancel = ttk.Button(self.window, text='Quit')
        # cancel.grid(row=2, column=2)

        self.window.mainloop()

    def addPipette(self, parent):

        pipette_type_label = tk.Label(parent, text="Pipette Type")
        pipette_type_label.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)

        self.combobox_value = tk.StringVar()
        pipette_types = ('p10_single', 'p10_multi')
        self.combobox_value.set(pipette_types[0])
        my_combobox = ttk.OptionMenu(parent, self.combobox_value, *pipette_types)
        my_combobox.grid(row=1, column=2)

        combobox_label = tk.Label(parent, text="Pipette Location")
        combobox_label.grid(row=2, column=1, sticky=tk.N + tk.E + tk.S + tk.W)

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
