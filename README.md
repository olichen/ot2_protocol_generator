[![ot2 robot](/docs/ot2-robot.jpg)](https://opentrons.com/ot-2/)

# OT2 Protocol Generator

> Provides a front-end interface to generate a protocol for the [OT-2 liquid handler](https://opentrons.com/ot-2/) using the [Opentrons API](https://docs.opentrons.com/v2/). Users use simple drop-down menus to select plates and pipettes, and input transfer volumes via a CSV file.

---

## Usage

![application window](/docs/app-window.png)

1. Select the pipette type and location.
2. Select the tip rack and plate types and locations for a transfer.
3. Select a CSV file by clicking the '..' button.
4. Click 'Generate' and select a folder to place the generated protocol

- To add another transfer, up to the maximum of 3 that can fit on the machine, click the 'Add' button.
- To remove a previously added transfer, click the 'Remove' button.

### CSV File Format

The CSV file must have the target well defined in the first cell of the column and the transfer volume in μL defined in the second cell of the column. See the [data folder](/data) for examples.

Well location|Transfer volume (μL)
---|---
A1|7.4
A2|3.6
A3|6.4
...|...
H12|4.2

### Adding New Labware

1. Identify the API Name of the new labware. To find labware, check the [opentrons labware library](https://labware.opentrons.com/). Make note of the 'API Name'.
2. Add the API Name to the protocol generator. Add the new labware to a 'labware.ini' file placed in the same folder as the protocol generator executable. Open the program and use the 'File' > 'Edit Labware' option to automatically generate a 'labware.ini' file.

### Creating Custom Labware

1. To create custom labware, use the [opentrons labware create tool](https://labware.opentrons.com/create/). Make note of the 'API Load Name'.
2. Add the custom labware to the Opentrons application. Open the Opentrons application. The Custom Labware menu can be found under 'More' > 'Custom Labware'.
3. Add the API Name to the protocol generator. Add the new labware to a 'labware.ini' file placed in the same folder as the protocol generator executable. Open the program and use the 'File' > 'Edit Labware' option to automatically generate a 'labware.ini' file.

---

## Setup

To run the program from command line, clone the repository and run 'cli.py'.

```shell
$ git clone https://github.com/olichen/ot2_protocol_generator.git
$ cd /ot2_protocol_generator
$ python cli.py
```

### Distribution

The program can be compiled into an executable with pyinstaller.

```shell
$ git clone https://github.com/olichen/ot2_protocol_generator.git
$ cd /ot2_protocol_generator
$ pip install pyinstaller
$ pyinstaller --onefile -w --name ot2_protocol_generator cli.py
```
