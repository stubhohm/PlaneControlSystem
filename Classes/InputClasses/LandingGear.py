from ..GeneralClasses.Attributes import BoolAtt, StrAtt

class LandingGear():
    def __init__(self) -> None:
        self.name = StrAtt('Landing Gear')
        self.stow_gear = BoolAtt(False)
        self.brakes = BoolAtt(True)
