from ..GeneralClasses.Attributes import Vect3Att

class Accelerometer():
    def __init__(self) -> None:
        self.orientation = Vect3Att()

    def set(self, value:Vect3Att):
        self.orientation.set(value)

    def get(self):
        return self.orientation.get()