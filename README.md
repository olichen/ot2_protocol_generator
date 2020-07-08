<a href="https://opentrons.com/ot-2/">
    <img src="/docs/ot2-robot.jpg" title="ot2 robot" alt="ot2 robot" height="300px">
</a>

# OT2 Protocol Generator

> Provides a front-end interface to generate a protocol for the [OT-2 liquid handler](https://opentrons.com/ot-2/) using the [Opentrons API](https://docs.opentrons.com/v2/). Users use simple drop-down menus to select plates and pipettes, and input transfer volumes via a CSV file.

---

## Usage

<img src="/docs/app-window.png" title="application window" alt="application window">

- Image goes here
- step by step
- etc etc

### CSV File Format

- placeholder

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
