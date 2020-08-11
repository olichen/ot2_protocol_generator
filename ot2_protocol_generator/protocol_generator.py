import tkinter as tk
from tkinter import ttk
from ot2_protocol_generator.gui import pipette_input_panel
from ot2_protocol_generator.gui import plate_input_panel
from ot2_protocol_generator.helpers import menu_helper


class ProtocolGenerator:
    def __init__(self):
        # Initialize window
        self.window = tk.Tk()
        self.window.title('Protocol Generator')
        self.window.resizable(False, False)

        # Initialize menu bar
        self._mh = menu_helper.MenuHelper()
        self._add_menubar()

        # Initialize the first input panel
        self._input_panels = []
        self._add_pipette()
        self._add_plate()

        # Initialize buttons along bottom of application
        self._create_bottom_menu()

    # Adds the File and Help menus
    def _add_menubar(self):
        menubar = tk.Menu(self.window)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Generate Protocol', command=self._save)
        filemenu.add_command(label='Edit Labware', command=self._mh.editLabware)
        filemenu.add_command(label='Quit', command=self._quit)
        menubar.add_cascade(label='File', menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='Help', command=self._mh.help)
        helpmenu.add_command(label='About', command=self._mh.about)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.window.config(menu=menubar)

    # Adds a pipette selector panel
    def _add_pipette(self):
        ip = pipette_input_panel.PipetteInputPanel(self.window)
        ip.grid(row=len(self._input_panels), sticky='nesw')
        self._input_panels.append(ip)

    # Add bottom menu: add transfer, remove transfer, generate protocol
    def _create_bottom_menu(self):
        frame = ttk.Frame(self.window)
        frame.grid(row=100, sticky='nesw')

        _save = ttk.Button(frame, text='Generate', width=12, command=self._save)
        _save.pack(side=tk.RIGHT)

        rem = ttk.Button(frame, text='Remove', width=12, command=self._rem_plate)
        rem.pack(side=tk.RIGHT)

        add = ttk.Button(frame, text='Add', width=12, command=self._add_plate)
        add.pack(side=tk.RIGHT)


    # Add a plate selector panel
    def _add_plate(self):
        if len(self._input_panels) < 4:
            ip = plate_input_panel.PlateInputPanel(self.window)
            ip.grid(row=len(self._input_panels), sticky='nesw')
            self._input_panels.append(ip)

    # Remove a plate input panel
    def _rem_plate(self):
        if len(self._input_panels) > 2:
            panel = self._input_panels.pop()
            panel.destroy()

    # Outputs the protocol to a file
    def _save(self):
        data = (ip.getData() for ip in self._input_panels)
        self._mh.save(self.window, *data)

    # Exit the application
    def _quit(self, event=None):
        self.window.destroy()
