# Helper class used to determine validity of 8 well transfers. Returns an
# array col_values that gives the volume to be transfered for each column
class EightTransfer:
    def __init__(self, volumedict):
        self.col_volumes = [None] * 12
        self.well_volumes = [[None for y in range(8)] for x in range(12)]
        self.readVolumeDict(volumedict)
        self.checkWells()

    # Read the values from volumedict into col_volumes
    def readVolumeDict(self, volumedict):
        for well, vol in volumedict.items():
            y = self.charToInt(well[0])
            x = int(well[1:])-1
            # If the well is empty, fill it with a volume, otherwise raise
            # an exception
            if not self.col_volumes[x]:
                self.col_volumes[x] = vol
            else:
                if not self.col_volumes[x] == vol:
                    err_str = "Volume for well '{0}' does not match {1}" \
                            .format(well, self.col_volumes[x])
                    raise ValueError(err_str)
            self.well_volumes[x][y] = vol

    # Check to make sure there is a volume in each well for each column
    # that has a volume in it
    def checkWells(self):
        for i in range(12):
            if self.col_volumes[i]:
                for j in range(8):
                    if not self.well_volumes[i][j]:
                        err_str = "Missing volume for well '{0}'" \
                                .format(chr(ord('A') + j) + str(i + 1))
                        raise IndexError

    # Converts the alphabetic component of the well to an integer
    # A = 0, B = 2, .., H = 8
    def charToInt(self, c):
        return ord(c)-ord('A')
