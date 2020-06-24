from dataclasses import dataclass


# Dataclass to hold the data that holds data related to the pipette
@dataclass
class PipetteData:
    pipette_name: str
    pipette_loc: str

    # Returns true if we have a multi channel pipette
    def isMulti(self):
        if 'multi' in self.pipette_name:
            return True
        elif 'single' in self.pipette_name:
            return False
        else:
            err_str = "Invalid pipette: '{0}'".format(self.pipette_name)
            raise ValueError(err_str)

