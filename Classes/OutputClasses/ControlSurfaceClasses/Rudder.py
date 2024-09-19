from Keys.Keys import left_rudder, right_rudder
from Keys.Keys import left, right
from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import StrAtt, BoolAtt

class Rudders():
    def __init__(self) -> None:
        self.left = Rudder(left_rudder, left)
        self.right = Rudder(right_rudder, right)

    def run(self):
        self.left.deploy()
        self.right.deploy()

    def return_to_zero(self):
        self.left.return_to_zero()
        self.right.return_to_zero()

    def print(self):
        self.left.print()
        self.right.print()

class Rudder(ControlSurface):
    def __init__(self, name, laterality:bool) -> None:
        super().__init__()
        self.name.set(name)
        self.laterality = BoolAtt(laterality)
    
    def deploy(self):
        if not self.move_to_target():
            print(f'{self.name.get()} is not in tolerance.')

    def retract(self):
        self.return_to_zero()
    
    def set_target_position(self, value: int):
        super().set_target_position(value)

    def print(self):
        print(f'\n{self.name.get()}')
        print(f'Current: {self.current_position.get()}')
        print(f'Target:{self.target_position.get()}')