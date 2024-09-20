from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import BoolAtt

class Wheel(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set(0)
        self.change_rate.set(1)
        self.target_tolerance.set(0)
        self.set_target_position(self.max_position.get())
        self.deploying = BoolAtt(False)
        self.deployed = BoolAtt(False)
        self.brakes_engaged = BoolAtt(False)

    def engage_brakes(self):
        self.brakes_engaged.set(True)

    def release_brakes(self):
        self.brakes_engaged.set(False)

    def get_brake_state(self):
        self.brakes_engaged.get()

    def set_wheel_bools(self):
        if self.current_position.get() == self.max_position.get():
            self.deploying.set(False)
            self.deployed.set(True)
        else:
            self.deploying.set(True)
            self.deployed.set(False)

    def get_wheel_bools(self):
        self.set_wheel_bools()
        return self.deployed.get(), self.deploying.get()

    def print_wheel_bools(self, position:str):
        self.set_wheel_bools()
        if self.deploying.get():
            print(f"Wheel on {position} is moving.")
            print(f"Ammount: {self.current_position.get()}")
        if self.deployed.get():
            print(f"Wheel on {position} is deployed.")
        if self.brakes_engaged.get():
            print(f"Wheel on {position} is braking.")
        if not self.deployed.get() and not self.deploying.get():
            print(f"Wheel on {position} is retracted.")
        print(self.target_position.get())

    def deploy(self):
        if not self.move_to_target():
            a = True
            #print(f'\n{self.name.get()} is not in tolerance.')
        self.set_wheel_bools()
        return self.deploying.get(), self.deployed.get()
     
    def retract(self):
        self.return_to_zero()
        self.set_wheel_bools()
        return self.deploying.get(), self.deployed.get()

class LandingGear():
    def __init__(self) -> None:
        self.left = Wheel()
        self.right = Wheel()
        self.front = Wheel()
        self.deploying = BoolAtt(False)
        self.deployed = BoolAtt(False)

    def run(self):
        self.left.move_to_target()
        self.right.move_to_target()
        self.front.move_to_target()

    def print_wheel_states(self):
        self.front.print_wheel_bools('Front')
        self.left.print_wheel_bools('Left')
        self.right.print_wheel_bools('Right')
            
    def deploy(self):
        a, d = self.left.deploy()
        b, e = self.right.deploy()
        c, f = self.front.deploy()
        if True in [a, b, c]:
            self.deploying.set(True)
        if True in [d, e, f] and False not in [d, e, f]:
            self.deployed.set(True)
    
    def retract(self):
        a, d = self.left.retract()
        b, e = self.right.retract()
        c, f = self.front.retract()
        if True in [a, b, c]:
            self.deploying.set(True)
        if False in [d, e, f] and True not in [d, e, f]:
            self.deployed.set(True)

    def engage_brakes(self):
        self.front.engage_brakes()
        self.left.engage_brakes()
        self.right.engage_brakes()

    def release_brakes(self):
        self.front.release_brakes()
        self.left.release_brakes()
        self.right.release_brakes()

    def print(self):
        print()
        self.print_wheel_states()
