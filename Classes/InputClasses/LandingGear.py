from ..GeneralClasses.Attributes import BoolAtt, StrAtt

class LandingGear():
    def __init__(self) -> None:
        self.name = StrAtt('Landing Gear')
        self.set_deployed = BoolAtt(False)
