from tkinter import filedialog
from tkinter import messagebox
from ot2_protocol_generator import protocol_writer
import webbrowser
import os
from platform import system
import subprocess
import logging
from ot2_protocol_generator.helpers import log_helper
from ot2_protocol_generator.helpers import config
import traceback


class MenuHelper:
    def __init__(self):
        # Initialize log handler
        self.lh = log_helper.LogHandler()
        logger = logging.getLogger()
        logger.addHandler(self.lh)

    # Outputs the protocol to a file
    def save(self, parent, *data):
        pw = protocol_writer.ProtocolWriter()

        try:
            # Read in data from each input panel. Throws an exception if
            # invalid data is encountered
            for d in data:
                pw.addData(d)

            if ofile := filedialog.asksaveasfilename(title='Save Protocol'):
                pw.saveOutput(ofile)

                if self.lh.text:
                    log_helper.WarningMessageBox(parent, self.lh.text)
                parent.destroy()
            else:
                self.lh.clear()
                parent.focus()
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror(title='Error', message=e)
            self.lh.clear()
            parent.focus()

    # Open the labware.ini file for editing
    def editLabware(self):
        if not os.path.exists('./labware.ini'):
            cfg = config.Configuration('./labware.ini')
            cfg.writeFile('./labware.ini')

        OS = system().lower()
        if 'windows' in OS:
            opener = 'start'
        elif 'osx' in OS or 'darwin' in OS:
            opener = 'open'
        else:
            opener = 'xdg-open'
        subprocess.run(opener + ' labware.ini', shell=True)
        msg = 'Please restart the protocol generator after editing any labware'
        messagebox.showinfo(title='Labware', message=msg)

    # Open the home page on github
    def help(self):
        url = 'https://github.com/olichen/ot2_protocol_generator#readme'
        webbrowser.open(url)

    # Pop open an about box
    def about(self):
        msg = ('Version 1.0\n'
               'Copyright (c) 2020 Oliver Chen\n'
               'https://github.com/olichen/ot2_protocol_generator')
        messagebox.showinfo(title='About', message=msg)
