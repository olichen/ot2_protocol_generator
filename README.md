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

- The CSV file must follow the following format:

Well location|Well volume (μL)
---|---
A1|7.4
A2|3.6
A3|6.4
...|...
H12|4.2

### Custom Labware

- To add custom labware to the protocol generator, add it to a a 'labware.ini' file placed in the same folder as the protocol generator executable. A [sample 'labware.ini' file](/labware.ini) can be found in the github repository..
- To find 

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
