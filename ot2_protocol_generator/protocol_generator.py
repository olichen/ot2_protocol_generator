import tkinter as tk
from tkinter import ttk
from .gui import pipette_input_panel
from .gui import plate_input_panel
from .helpers import menu_helper


class ProtocolGenerator:
    def __init__(self):
        # Initialize window
        self.window = tk.Tk()
        self.window.title('Protocol Generator')
        self.window.resizable(False, False)

        # Initialize menu bar
        self.mh = menu_helper.MenuHelper()
        self.addMenubar()

        # Initialize the first input panel
        self.input_panels = []
        self.addPipette()
        self.addPlate()

        # Initialize buttons along bottom of application
        self.createBottomMenu()

    # Adds the File and Help menus
    def addMenubar(self):
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Generate Protocol', command=self.save)
        filemenu.add_command(label='Edit Labware', command=self.mh.editLabware)
        filemenu.add_command(label='Quit', command=self.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help', command=self.mh.help)
        helpmenu.add_command(label='About', command=self.mh.about)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.window.config(menu=menubar)

    # Adds a pipette selector panel
    def addPipette(self):
        ip = pipette_input_panel.PipetteInputPanel(self.window)
        ip.grid(row=len(self.input_panels), sticky='nesw')
        self.input_panels.append(ip)

    # Add a plate selector panel
    def addPlate(self):
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

        rem = ttk.Button(frame, text='Remove', width=12, command=self.remPlate)
        rem.pack(side=tk.RIGHT)

        add = ttk.Button(frame, text='Add', width=12, command=self.addPlate)
        add.pack(side=tk.RIGHT)

    # Remove a plate input panel
    def remPlate(self):
        if len(self.input_panels) > 2:
            panel = self.input_panels.pop()
            panel.destroy()

    # Outputs the protocol to a file
    def save(self):
        data = (ip.getData() for ip in self.input_panels)
        self.mh.save(self.window, *data)

    # Exit the application
    def quit(self, event=None):
        self.window.destroy()
