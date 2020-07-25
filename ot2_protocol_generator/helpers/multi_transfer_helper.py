# Helper class that returns an array col_volumes that gives the volume to be
# transferred for each column.
class MultiTransferHelper:
    def __init__(self, volumedict):
        self.col_volumes = [None] * 12
        self.well_volumes = [[None for y in range(8)] for x in range(12)]
        self.readVolumeDict(volumedict)
        self.checkWells()

    # Read the values from volumedict into col_volumes and well_volumes
    def readVolumeDict(self, volumedict):
        for well, vol in volumedict.items():
            (x, y) = self.wellToIndex(well)

            self.well_volumes[x][y] = vol
            if self.col_volumes[x] is None:
                self.col_volumes[x] = vol

    # Check every well of the plate against the recorded col_volumes
    def checkWells(self):
        for i, column in enumerate(self.well_volumes, 1):
            for vol in column:
                if vol != self.col_volumes[i]:
                    err_str = (f"Volumes in column A{i} through H{i}"
                               " do not match.")
                    raise ValueError(err_str)

    # Converts a well input to an index
    def wellToIndex(self, well: str) -> (int, int):
        x = int(well[1:]) - 1
        y = ord(well[0]) - ord('A')
        return (x, y)
