from ..GeneralClasses.Attributes import Vect3Att, StrAtt

class TargetOrientation():
    def __init__(self) -> None:
        self.name = StrAtt('Target Orientation')
        self.vector = Vect3Att()