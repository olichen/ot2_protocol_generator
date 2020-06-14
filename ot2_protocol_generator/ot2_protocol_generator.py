import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import protocol_data
import protocol_writer
import protocol_gui


class OT2ProtocolGenerator:
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

    def createGUI(self):
        pg = protocol_gui.ProtocolGUI(self.window)

        pg.addPipetteSelectors(self.pipette_type, self.pipette_loc)
        pg.addTipRackSelectors(self.tip_rack_type, self.tip_rack_loc)
        pg.addSourcePlateSelectors(self.src_plate_type, self.src_plate_loc)
        pg.addDestPlateSelectors(self.dest_plate_type, self.dest_plate_loc)
        pg.addCSVSelector(self.csv_file_loc)

        frame = ttk.Frame(self.window)
        frame.grid(row=101, column=1, columnspan=4, sticky='nesw')
        self.addSaveCancel(frame)

    def addSaveCancel(self, parent):
        save = ttk.Button(parent, text='Generate Protocol', command=self.save)
        save.grid(row=1, column=1)
        cancel = ttk.Button(parent, text='Quit', command=self.quit)
        cancel.grid(row=1, column=2)
        self.window.bind('<Escape>', self.quit)

    def save(self):
        data = self.getProtocolData()
        try:
            data.isValid()
            pw = protocol_writer.ProtocolWriter(data)

            output_file = self.outputFileDialog()
            pw.saveOutput(output_file)
            self.quit()
        except Exception as e:
            messagebox.showerror(title='Error', message=e)
            self.window.focus()

    def outputFileDialog(self):
        return filedialog.asksaveasfilename(
            title='Save protocol',
            filetypes=[('Python Files', '*.py')])

    def getProtocolData(self):
        return protocol_data.ProtocolData(
            tip_rack_type=self.tip_rack_type.get(),
            tip_rack_loc=self.tip_rack_loc.get(),
            src_plate_type=self.src_plate_type.get(),
            src_plate_loc=self.src_plate_loc.get(),
            dest_plate_type=self.dest_plate_type.get(),
            dest_plate_loc=self.dest_plate_loc.get(),
            pipette_type=self.pipette_type.get(),
            pipette_loc=self.pipette_loc.get(),
            csv_file_loc=self.csv_file_loc.get())

    def quit(self, event=None):
        self.window.destroy()

    def main(self):
        self.window.mainloop()


if __name__ == "__main__":
    OT2ProtocolGenerator().main()
