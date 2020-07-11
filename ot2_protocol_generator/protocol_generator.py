import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from . import protocol_writer
from .gui import pipette_input_panel
from .gui import plate_input_panel
from .gui import config
import logging
from .helpers import log_helper
import traceback
import webbrowser
import os


class ProtocolGenerator:
    def __init__(self):
        # Initialize window
        self.window = tk.Tk()
        self.window.title('Protocol Generator')
        self.window.resizable(False, False)

        # Initialize the first input panel
        self.input_panels = []
        self.addMenubar()
        self.addPipettePanel()
        self.addPlatePanel()
        self.createBottomMenu()

        # Initialize log handler (outputs to self.log_text)
        self.log_text = ['']
        lh = log_helper.LogHandler(self.log_text)
        logger = logging.getLogger()
        logger.addHandler(lh)

    def addMenubar(self):
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Generate Protocol', command=self.save)
        filemenu.add_command(label='Edit Labware', command=self.editLabware)
        filemenu.add_command(label='Quit', command=self.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help', command=self.help)
        helpmenu.add_command(label='About', command=self.about)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.window.config(menu=menubar)

    # Adds a pipette selector panel
    def addPipettePanel(self):
        ip = pipette_input_panel.PipetteInputPanel(self.window)
        ip.grid(row=len(self.input_panels), sticky='nesw')
        self.input_panels.append(ip)

    # Add a plate selector panel
    def addPlatePanel(self):
        if len(self.input_panels) < 4:
            ip = plate_input_panel.PlateInputPanel(self.window)
            ip.grid(row=len(self.input_panels), sticky='nesw')
            self.input_panels.append(ip)

    # Add bottom menu: add transfer, remove transfer, generate protocol
    def createBottomMenu(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=100, sticky='nesw')

        save = ttk.Button(frame, text='Generate', width=12, command=self.save)
        save.pack(side=tk.RIGHT)

        addInput = ttk.Button(frame, text='Remove', width=12, command=self.remPlatePanel)
        addInput.pack(side=tk.RIGHT)

        addInput = ttk.Button(frame, text='Add', width=12, command=self.addPlatePanel)
        addInput.pack(side=tk.RIGHT)

    # Remove a plate input panel
    def remPlatePanel(self):
        if len(self.input_panels) > 2:
            panel = self.input_panels.pop()
            panel.destroy()

    # Outputs the protocol to a file
    def save(self):
        pw = protocol_writer.ProtocolWriter()

        try:
            for ip in self.input_panels:
                pw.addData(ip.getData())

            output_file = filedialog.asksaveasfilename(title='Save protocol')
            if output_file:
                pw.saveOutput(output_file)

                if self.log_text[0]:
                    log_helper.WarningMessageBox(self.window, self.log_text[0])
                self.quit()
            else:
                self.log_text[0] = ''
                self.window.focus()
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror(title='Error', message=e)
            self.log_text[0] = ''
            self.window.focus()

    def editLabware(self):
        #with open(output_file, 'w') as f:
        cfg = config.Configuration()
        ','.join(cfg.TIP_RACK_NAMES)
        print(cfg.TIP_RACK_LOCS)

    # Exit the application
    def quit(self, event=None):
        self.window.destroy()

    def help(self):
        url = 'https://github.com/olichen/ot2_protocol_generator#readme'
        webbrowser.open(url)

    def about(self):
        msg = 'Version 1.0\nCopyright (c) 2020 Oliver Chen'
        messagebox.showinfo(title='About', message=msg)
