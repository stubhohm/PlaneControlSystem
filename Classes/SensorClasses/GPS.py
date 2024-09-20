from ..GeneralClasses.Attributes import Vect3Att

class GPS():
    def __init__(self) -> None:
        self.position = Vect3Att()

    def set(self, value:Vect3Att):
        self.position.set(value)

    def get(self):
        return self.position.get()