import tkinter as tk
from tkinter import ttk

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Protocol Generator')

        pipette_frame = ttk.LabelFrame(self.window, text="Pipette")
        pipette_frame.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.addPipette(pipette_frame)

        self.combobox_value = tk.StringVar()
        self.window.mainloop()

    def addPipette(self, pipette_frame):

        pipette_type_label = tk.Label(pipette_frame, text="Pipette Type")
        pipette_type_label.grid(row=1, column=1, sticky=tk.N + tk.E + tk.S + tk.W)

        self.combobox_value = tk.StringVar()
        my_combobox = ttk.Combobox(pipette_frame, height=4, textvariable=self.combobox_value)
        my_combobox.grid(row=1, column=2)
        my_combobox['values'] = ('p10_single', 'p10_multi')
        my_combobox.current(0)

        combobox_label = tk.Label(pipette_frame, text="Pipette Location")
        combobox_label.grid(row=2, column=1, sticky=tk.N + tk.E + tk.S + tk.W)

    def addSaveCancel(self):
        print('placeholder')


    def main(self):
        print('placeholder')


if __name__ == "__main__":
    GUI().main()
