import logging
import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
from tkinter import scrolledtext


# Log handler that reroutes emitted messages to a string
class LogHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
        self.text = ''

    def emit(self, record):
        msg = self.format(record)
        self.text += msg
        self.text += '\n'

    def clear(self):
        self.text = ''


# Warning message box that displays all the warnings
class WarningMessageBox(Toplevel):
    def __init__(self, parent, text):

        # Initialize an un-resizable Toplevel message box
        Toplevel.__init__(self, parent)
        self.title('Warning')
        self.resizable(False, False)

        # Add the scrolled-text object that displays all the warnings
        frame = ttk.Frame(self)
        frame.grid(sticky='nesw')
        st = scrolledtext.ScrolledText(frame, width=80, height=20)
        st.grid(row=0, sticky='nesw', padx=10, pady=10)
        st.insert(tk.INSERT, text)
        st.configure(state='disabled')

        # Add an 'ok' button to close the message box
        # Also bind <Escape> and <Return> to close
        ok_button = ttk.Button(frame, text='Ok', command=self.quit)
        ok_button.grid(row=1, padx=10, pady=10)
        self.bind('<Escape>', self.quit)
        self.bind('<Return>', self.quit)

        # Wait for the message box to appear, then grab all input (disables
        # main window) and wait for the user to close the box
        self.wait_visibility()
        self.grab_set()
        self.wait_window(self)

    def quit(self, event=None):
        self.destroy()
