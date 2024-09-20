from Keys.Keys import left_rudder, right_rudder
from Keys.Keys import left, right
from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import BoolAtt, Vect3Att

class Rudders():
    def __init__(self) -> None:
        self.left = Rudder(left_rudder, left)
        self.right = Rudder(right_rudder, right)

    def set_positions(self, control_input:Vect3Att, trim = False):
        roll = control_input.x.get()
        pitch = control_input.y.get()
        yaw = control_input.z.get()
        self.set_position(roll, pitch, yaw, trim)

    def set_trim(self, control_input:Vect3Att):
        trim = True
        self.set_positions(control_input, trim)

    def set_position(self, roll, pitch, yaw, trim:bool):
        self.left.set_position(roll, pitch, yaw, trim)
        self.right.set_position(roll, pitch, yaw, trim)

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
        if trim:
            yaw = int(yaw / 2)
        return yaw
    
    def set_pitch(self, pitch:int, trim:bool):
        if self.laterality.get() == left:
            pitch *= -1 
        if trim:
            pitch = int(pitch / 2)
            return pitch
        else:
            return pitch
    
    def set_roll(self, roll, trim:bool):
        return 0

    def print(self):
        print(f'\n{self.name.get()}')
        print(f'Current: {self.current_position.get()}')
        print(f'Target:{self.target_position.get()}')