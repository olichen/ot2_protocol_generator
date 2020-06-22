import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from . import protocol_data
from . import protocol_writer
from . import gui_helper
from . import csv_reader
import logging
from . import log_handler


class ProtocolGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Protocol Generator')

        self.gui = gui_helper.InputPanel(self.window)
        self.createSaveCancelButtons()

        self.log_text = ['']
        lh = log_handler.LogHandler(self.log_text)
        logger = logging.getLogger()
        logger.addHandler(lh)

    def createSaveCancelButtons(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=101, column=1, columnspan=4, sticky='nesw')

        cancel = ttk.Button(frame, text='Cancel', command=self.quit)
        cancel.pack(side=tk.RIGHT)
        self.window.bind('<Escape>', self.quit)

        save = ttk.Button(frame, text='Generate Protocol', command=self.save)
        save.pack(side=tk.RIGHT)

    def save(self):
        data = self.gui.getProtocolData()
        try:
            data.isValid()
            csv_data = csv_reader.CSVReader(data.csv_file_loc)
            pw = protocol_writer.ProtocolWriter()
            pw.addInput(data, csv_data)

            output_file = filedialog.asksaveasfilename(title='Save protocol')
            pw.saveOutput(output_file)
            if self.log_text[0]:
                messagebox.showwarning(title='Warning', message=self.log_text[0])
            self.quit()
        except Exception as e:
            messagebox.showerror(title='Error', message=e)
            self.window.focus()

    def quit(self, event=None):
        self.window.destroy()
