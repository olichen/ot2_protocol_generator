[![ot2 robot](/docs/ot2-robot.jpg)](https://opentrons.com/ot-2/)

# OT2 Protocol Generator

> Provides a front-end interface to generate a protocol for the [OT-2 liquid handler](https://opentrons.com/ot-2/) using the [Opentrons API](https://docs.opentrons.com/v2/). Users use simple drop-down menus to select plates and pipettes, and input transfer volumes via a CSV file.

---

## Usage

![application window](/docs/app-window.png)

- Select the pipette type and location.
- Select the tip rack and plate types and locations for a transfer.
- Select a CSV file by clicking the '..' button.
- To add another transfer, up to the maximum of 3 that can fit on the machine, click the 'Add' button.
- To remove a previously added transfer, click the 'Remove' button.
- Click 'Generate' and select a folder to place the generated protocol

### CSV File Format

- The CSV file must follow the following format:

Well location|Well volume (μL)
--|---
A1|7.4
A2|3.6
A3|6.4

### Custom Labware

- placeholder

---

## Setup

Running the the program from command line:

```shell
$ git clone https://github.com/olichen/ot2_protocol_generator.git
$ cd /ot2_protocol_generator
$ python cli.py
```

### Distribution

Compiling the program into an executable for distribution:

```shell
$ git clone https://github.com/olichen/ot2_protocol_generator.git
$ cd /ot2_protocol_generator
$ pip install pyinstaller
$ pyinstaller --onefile -w --name ot2_protocol_generator cli.py
```

---

## Structure

```
etc
etc
```
