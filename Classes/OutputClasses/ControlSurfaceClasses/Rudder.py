from ....Keys.Keys import left_rudder, right_rudder
from ....Keys.Keys import left, right
from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import StrAtt, BoolAtt

class Rudders():
    def __init__(self) -> None:
        self.left = Rudder(left_rudder, left)
        self.right = Rudder(right_rudder, right)

class Rudder(ControlSurface):
    def __init__(self, name, laterality:bool) -> None:
        super().__init__()
        self.name.set_value(name)
        self.laterality = BoolAtt(laterality)
    
    def deploy(self):
        self.move_to_target()

    def retract(self):
        self.return_to_zero()
    
    def set_target_position(self, value: int):
        super().set_target_position(value)