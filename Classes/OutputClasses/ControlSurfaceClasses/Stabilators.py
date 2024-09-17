from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import StrAtt, BoolAtt

class Stabilators(ControlSurface):
    def __init__(self, name, laterality:str, proximal:bool) -> None:
        super().__init__()
        self.name.set_value(name)
        self.laterality = StrAtt(laterality)
        self.proximal = BoolAtt(proximal)
    
    def deploy(self):
        self.move_to_target()

    def retract(self):
        self.return_to_zero()
    
    def set_target_position(self, value: int):
        super().set_target_position(value)