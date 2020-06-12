import tkinter as tk
from tkinter import filedialog
import csv_reader
import output_writer
import protocol_data


class ProtocolGenerator:
    def __init__(self, data):
        self.data = data

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
            f1.write(ow.getTipRack(self.data.tip_rack_type, self.data.tip_rack_loc))
            f1.write(ow.getSrcPlate(self.data.src_plate_type, self.data.src_plate_loc))
            f1.write(ow.getDestPlate(self.data.dest_plate_type, self.data.dest_plate_loc))
            f1.write(ow.getPipette(self.data.pipette_type, self.data.pipette_loc))

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
    data = protocol_data.ProtocolData(
        tip_rack_type='geb_96_tiprack_10ul',
        tip_rack_loc='1',
        src_plate_type='appliedbiosystems_96_wellplate_100ul',
        src_plate_loc='2',
        dest_plate_type='appliedbiosystems_96_wellplate_100ul',
        dest_plate_loc='3',
        pipette_type='p10_single',
        pipette_loc='right',
        csv_file_loc='placeholder')
    pg = ProtocolGenerator(data)
    pg.main()
