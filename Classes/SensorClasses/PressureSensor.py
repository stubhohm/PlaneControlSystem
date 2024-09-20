from ..GeneralClasses.Attributes import IntAtt

class Barometer():
    def __init__(self) -> None:
        self.delta_p = IntAtt()

    def set(self, value:int):
        self.delta_p.set(value)

    def get(self):
        return self.delta_p.get()