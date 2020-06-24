import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from . import protocol_writer
from .gui import pipette_input_panel
from .gui import plate_input_panel
from . import csv_reader
import logging
from . import log_handler
import traceback


class ProtocolGenerator:
    def __init__(self):
        # Initialize window
        self.window = tk.Tk()
        self.window.title('Protocol Generator')

        # Initialize the first input panel
        self.input_panels = []
        self.addPipettePanel()
        self.addPlatePanel()
        self.createAddRemoveButtons()
        self.createSaveCancelButtons()

        # Initialize log handler (outputs to self.log_text)
        self.log_text = ['']
        lh = log_handler.LogHandler(self.log_text)
        logger = logging.getLogger()
        logger.addHandler(lh)

    def addPipettePanel(self):
        frame=ttk.Frame(self.window)
        frame.grid(row=len(self.input_panels), sticky='nesw')
        ip = pipette_input_panel.PipetteInputPanel(frame)
        self.input_panels.append(ip)

    # Add a set of input panels
    def addPlatePanel(self):
        frame=ttk.Frame(self.window)
        frame.grid(row=len(self.input_panels), sticky='nesw')
        ip = plate_input_panel.PlateInputPanel(frame)
        self.input_panels.append(ip)

    # Create the save and cancel buttons
    def createAddRemoveButtons(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=100, sticky='nesw')

        addInput = ttk.Button(frame, text='+', command=self.addPlatePanel)
        addInput.pack(side=tk.RIGHT)

        # save = ttk.Button(frame, text='Generate Protocol', command=self.save)
        # save.pack(side=tk.RIGHT)

    # Create the save and cancel buttons
    def createSaveCancelButtons(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=101, sticky='nesw')

        cancel = ttk.Button(frame, text='Cancel', command=self.quit)
        cancel.pack(side=tk.RIGHT)
        self.window.bind('<Escape>', self.quit)

        save = ttk.Button(frame, text='Generate Protocol', command=self.save)
        save.pack(side=tk.RIGHT)

    def save(self):
        pw = protocol_writer.ProtocolWriter()

        for ip in self.input_panels:
            data = ip.getProtocolData()
            try:
                data.isValid()
                csv_data = csv_reader.CSVReader(data.csv_file_loc)
                pw.addInput(data, csv_data)
            except Exception as e:
                self.handleException(e)

        output_file = filedialog.asksaveasfilename(title='Save protocol')
        try:
            pw.saveOutput(output_file)
        except Exception as e:
            self.handleException(e)

        if self.log_text[0]:
            messagebox.showwarning(title='Warning', message=self.log_text[0])
        self.quit()

    def handleException(self, e):
        traceback.print_exc()
        messagebox.showerror(title='Error', message=e)
        self.window.focus()

    def quit(self, event=None):
        self.window.destroy()
