import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from . import protocol_data
from . import protocol_writer
from . import protocol_gui
from . import csv_reader
import logging
from . import log_handler


class OT2ProtocolGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Protocol Generator')

        self.tip_rack_name = tk.StringVar()
        self.tip_rack_loc = tk.StringVar()
        self.src_plate_name = tk.StringVar()
        self.src_plate_loc = tk.StringVar()
        self.dest_plate_name = tk.StringVar()
        self.dest_plate_loc = tk.StringVar()
        self.pipette_name = tk.StringVar()
        self.pipette_loc = tk.StringVar()
        self.csv_file_loc = tk.StringVar()

        self.createGUI()

        self.log_text = ['']
        lh = log_handler.LogHandler(self.log_text)
        logger = logging.getLogger()
        logger.addHandler(lh)

    def createGUI(self):
        pg = protocol_gui.ProtocolGUI(self.window)

        pg.createPipetteSelectors(self.pipette_name, self.pipette_loc)
        pg.createTipRackSelectors(self.tip_rack_name, self.tip_rack_loc)
        pg.createSourcePlateSelectors(self.src_plate_name, self.src_plate_loc)
        pg.createDestPlateSelectors(self.dest_plate_name, self.dest_plate_loc)
        pg.createCSVSelector(self.csv_file_loc)
        self.createSaveCancelButtons()

    def createSaveCancelButtons(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=101, column=1, columnspan=4, sticky='nesw')

        cancel = ttk.Button(frame, text='Cancel', command=self.quit)
        cancel.pack(side=tk.RIGHT)
        self.window.bind('<Escape>', self.quit)

        save = ttk.Button(frame, text='Generate Protocol', command=self.save)
        save.pack(side=tk.RIGHT)

    def save(self):
        data = self.getProtocolData()
        try:
            data.isValid()
            csv_data = csv_reader.CSVReader(data.csv_file_loc)
            pw = protocol_writer.ProtocolWriter(data, csv_data)

            output_file = self.outputFileDialog()
            pw.saveOutput(output_file)
            if self.log_text[0]:
                messagebox.showwarning(title='Warning', message=self.log_text[0])
            self.quit()
        except Exception as e:
            messagebox.showerror(title='Error', message=e)
            self.window.focus()

    def outputFileDialog(self):
        return filedialog.asksaveasfilename(
            title='Save protocol',
            filetypes=[('Python Files', '*.py')])

    def getProtocolData(self):
        ptype = self.getPipetteType(self.pipette_name.get())

        return protocol_data.ProtocolData(
                tip_rack_name=self.tip_rack_name.get(),
                tip_rack_loc=self.tip_rack_loc.get(),
                src_plate_name=self.src_plate_name.get(),
                src_plate_loc=self.src_plate_loc.get(),
                dest_plate_name=self.dest_plate_name.get(),
                dest_plate_loc=self.dest_plate_loc.get(),
                pipette_name=self.pipette_name.get(),
                pipette_loc=self.pipette_loc.get(),
                pipette_type=ptype,
                csv_file_loc=self.csv_file_loc.get())

    def getPipetteType(self, pname):
        if 'single' in pname:
            return 'single'
        elif 'multi' in pname:
            return 'multi'
        else:
            err_str = "Invalid pipette: '{0}'".format(pname)
            raise ValueError(err_str)

    def quit(self, event=None):
        self.window.destroy()
