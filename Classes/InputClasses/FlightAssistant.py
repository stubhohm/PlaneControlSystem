from ..GeneralClasses.Attributes import BoolAtt, StrAtt

class FlightAssistant():
    def __init__(self) -> None:
        self.name = StrAtt('Flight Assistant')
        self.set_deployed = BoolAtt(False)