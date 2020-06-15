# Helper class used to determine validity of 8 well transfers
class EightTransfer:
    def __init__(self, volumedict):
        self.col_volumes = [None] * 12
        self.well_volumes = [[None for y in range(8)] for x in range(12)]
        self.readVolumeDict(volumedict)
        self.checkWells()

    def readVolumeDict(self, volumedict):
        for well, vol in volumedict.items():
            y = self.charToInt(well[0])
            x = int(well[1:])-1
            if not self.col_volumes[x]:
                self.col_volumes[x] = vol
            else:
                if not self.col_volumes[x] == vol:
                    raise Exception
            self.well_volumes[x][y] = vol

    def checkWells(self):
        for i in range(12):
            if self.col_volumes[i]:
                for j in range(8):
                    if not self.well_volumes[i][j]:
                        raise IndexError

    def charToInt(self, c):
        return ord(c)-ord('A')
