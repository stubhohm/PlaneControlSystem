from Keys.Keys import left_inboard, left_outboard
from Keys.Keys import right_inboard, right_outboard
from Keys.Keys import left, right, proximal, distal
from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import StrAtt, BoolAtt


class Elevons():
    def __init__(self) -> None:
        self.left_outboard = Elevon(left_outboard, left, distal)
        self.left_inboard = Elevon(left_inboard, left, proximal)
        self.right_inboard = Elevon(right_inboard, right, proximal)
        self.right_outboard = Elevon(right_outboard, right, distal)

    def run(self):
        self.left_inboard.deploy()
        self.left_outboard.deploy()
        self.right_inboard.deploy()
        self.right_outboard.deploy()

    def return_to_zero(self):
        self.left_inboard.return_to_zero()
        self.left_outboard.return_to_zero()
        self.right_inboard.return_to_zero()
        self.right_outboard.return_to_zero()

    def print(self):
        self.left_inboard.print()
        self.left_outboard.print()
        self.right_inboard.print()
        self.right_outboard.print()

class Elevon(ControlSurface):
    def __init__(self, name, laterality:bool, proximal:bool) -> None:
        super().__init__()
        self.name.set(name)
        self.laterality = BoolAtt(laterality)
        self.proximal = BoolAtt(proximal)
    
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