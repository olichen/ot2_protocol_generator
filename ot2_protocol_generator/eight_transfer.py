# Helper class used to determine validity of 8 well transfers
class EightTransfer
    def __init__(self, volumedict):
        self.volumedict = volumedict
        self.col_volumes = [None] * 12
        self.well_volumes = [[None for y in range(8)] for x in range(12)]

    def charToInt(self, c):
        return ord(c)-ord('A')
