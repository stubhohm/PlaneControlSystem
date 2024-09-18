from ..GeneralClasses.Attributes import IntAtt, StrAtt

class TargetThrottle():
    def __init__(self) -> None:
        self.name = StrAtt('Target Orientation')
        self.throttle = IntAtt(0)