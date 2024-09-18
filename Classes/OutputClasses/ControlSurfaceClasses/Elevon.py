from ....Keys.Keys import left_inboard, left_outboard
from ....Keys.Keys import right_inboard, right_outboard
from ....Keys.Keys import left, right, proximal, distal
from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import StrAtt, BoolAtt


class Elevons():
    def __init__(self) -> None:
        self.left_outboard = Elevon(left_outboard, left, distal)
        self.left_inboard = Elevon(left_inboard, left, proximal)
        self.right_inboard = Elevon(right_inboard, right, proximal)
        self.right_outboard = Elevon(right_outboard, right, distal)

class Elevon(ControlSurface):
    def __init__(self, name, laterality:bool, proximal:bool) -> None:
        super().__init__()
        self.name.set_value(name)
        self.laterality = BoolAtt(laterality)
        self.proximal = BoolAtt(proximal)
    
    def deploy(self):
        self.move_to_target()

    def retract(self):
        self.return_to_zero()
    
    def set_target_position(self, value: int):
        super().set_target_position(value)