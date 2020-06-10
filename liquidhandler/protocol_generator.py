import tkinter as tk
from tkinter import filedialog
import csv_reader
import output_writer


class ProtocolGenerator:
    def __init__(self):
        self.tip_rack_type = 'geb_96_tiprack_10ul'
        self.tip_rack_loc = 1
        self.src_plate_type = 'appliedbiosystems_96_wellplate_100ul'
        self.src_plate_loc = 2
        self.dst_plate_type = 'appliedbiosystems_96_wellplate_100ul'
        self.dst_plate_loc = 3
        self.pipette_type = 'p10_single'
        self.pipette_loc = 'right'

    def main(self):
        file_path = self.getCSVFile()
        csvr = csv_reader.CSVReader(file_path)
        print(csvr.volumes)
        file_path = self.getOutputFile()
        self.saveOutput(file_path, csvr.volumes.items())

    def saveOutput(self, output_file, csv_volumes):
        ow = output_writer.OutputWriter()

        with open(output_file, 'w') as f1:
            f1.write(ow.getHeader())
            f1.write(ow.getTipRack(self.tip_rack_type, self.tip_rack_loc))
            f1.write(ow.getSrcPlate(self.src_plate_type, self.src_plate_loc))
            f1.write(ow.getDestPlate(self.dst_plate_type, self.dst_plate_loc))
            f1.write(ow.getPipette(self.pipette_type, self.pipette_loc))

            for well, volume in csv_volumes:
                f1.write(ow.getSingleTransfer(volume, well))

    def getCSVFile(self):
        root = tk.Tk()
        root.withdraw()
        return filedialog.askopenfilename(
            title='Select a file',
            filetypes=[('CSV Files', '*.csv')])

    def getOutputFile(self):
        root = tk.Tk()
        root.withdraw()
        files = [('Python Files', '*.py')]
        return filedialog.asksaveasfilename(
            title='Save output file',
            filetypes=files)


if __name__ == "__main__":
    ProtocolGenerator().main()
