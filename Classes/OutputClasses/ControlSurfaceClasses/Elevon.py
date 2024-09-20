from Keys.Keys import left_inboard, left_outboard
from Keys.Keys import right_inboard, right_outboard
from Keys.Keys import left, right, proximal, distal
from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import BoolAtt, Vect3Att


class Elevons():
    def __init__(self) -> None:
        self.left_outboard = Elevon(left_outboard, left, distal)
        self.left_inboard = Elevon(left_inboard, left, proximal)
        self.right_inboard = Elevon(right_inboard, right, proximal)
        self.right_outboard = Elevon(right_outboard, right, distal)

    def set_positions(self, control_input:Vect3Att, trim = False):
        roll = control_input.x.get()
        pitch = control_input.y.get()
        yaw = control_input.z.get()
        self.set_position(roll, pitch, yaw, trim)

    def set_trim(self, control_input:Vect3Att):
        trim =True
        self.set_positions(control_input, trim)

    def set_position(self, roll, pitch, yaw, trim:bool):
        self.left_inboard.set_position(roll, pitch, yaw, trim)
        self.left_outboard.set_position(roll, pitch, yaw, trim)
        self.right_inboard.set_position(roll, pitch, yaw, trim)
        self.right_outboard.set_position(roll, pitch, yaw, trim)

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
            return
            #print(f'\n{self.name.get()} is not in tolerance.')

    def retract(self):
        self.return_to_zero()

    def set_position(self, roll, pitch, yaw, trim):
        r = self.set_roll(roll, trim)
        p = self.set_pitch(pitch, trim)
        y = self.set_yaw(yaw, trim)
        summation = int(r + p + y)
        if trim:
            self.set_target_trim(summation)
        else:
            self.set_target_position(summation)

    def set_yaw(self, yaw, trim:bool):
        return 0
    
    def set_pitch(self, pitch:int, trim:bool):
        if self.proximal:
            pitch = int(pitch / 2)
        if trim:
            pitch = int(pitch / 2)
            return pitch
        else:
            return pitch
    
    def set_roll(self, roll, trim:bool):
        if self.laterality.get() == left:
            roll *= -1
        if self.proximal:
            roll = int(roll / 2)
        if trim:
            return roll
        else:
            return roll

    def set_target_position(self, value: int):
        super().set_target_position(value)

    def set_target_trim(self, value: int):
        return super().set_target_trim(value)

    def print(self):
        print(f'\n{self.name.get()}')
        print(f'Current: {self.current_position.get()}')
        print(f'Target:{self.target_position.get()}')