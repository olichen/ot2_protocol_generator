import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from . import protocol_writer
from .gui import pipette_input_panel
from .gui import plate_input_panel
import logging
from .helpers import log_helper
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
        lh = log_helper.LogHandler(self.log_text)
        logger = logging.getLogger()
        logger.addHandler(lh)

    # Adds a pipette selector panel
    def addPipettePanel(self):
        ip = pipette_input_panel.PipetteInputPanel(self.window)
        ip.frame.grid(row=len(self.input_panels), sticky='nesw')
        self.input_panels.append(ip)

    # Add a plate selector panel
    def addPlatePanel(self):
        ip = plate_input_panel.PlateInputPanel(self.window)
        ip.frame.grid(row=len(self.input_panels), sticky='nesw')
        self.input_panels.append(ip)

    # Add buttons to add or delete plate input panels
    def createAddRemoveButtons(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=100, sticky='nesw')

        addInput = ttk.Button(frame, text='+', command=self.addPlatePanel)
        addInput.pack(side=tk.RIGHT)

        addInput = ttk.Button(frame, text='-', command=self.remPlatePanel)
        addInput.pack(side=tk.RIGHT)

    # Remove a plate input panel
    def remPlatePanel(self):
        if len(self.input_panels) > 2:
            panel = self.input_panels.pop()
            panel.destroy()

    # Create the generate and cancel buttons
    def createSaveCancelButtons(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=101, sticky='nesw')

        cancel = ttk.Button(frame, text='Cancel', command=self.quit)
        cancel.pack(side=tk.RIGHT)
        self.window.bind('<Escape>', self.quit)

        save = ttk.Button(frame, text='Generate Protocol', command=self.save)
        save.pack(side=tk.RIGHT)

    # Outputs the protocol to a file
    def save(self):
        pw = protocol_writer.ProtocolWriter()

        for ip in self.input_panels:
            data = ip.getData()
            try:
                pw.addData(data)
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

    # Handles an exception; prints a traceback to console and pops up an
    # error box for the user
    def handleException(self, e):
        traceback.print_exc()
        messagebox.showerror(title='Error', message=e)
        self.window.focus()

    # Exit the application
    def quit(self, event=None):
        self.window.destroy()
