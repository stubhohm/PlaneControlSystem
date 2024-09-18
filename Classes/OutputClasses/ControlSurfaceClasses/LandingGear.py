from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import BoolAtt

class Wheel(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set_value(0)
        self.change_rate.set_value(1)
        self.deploying = BoolAtt(False)
        self.deployed = BoolAtt(False)

    def set_wheel_bools(self):
        if self.__current_position.get_value() == self.max_position.get_value():
            self.deploying.set_value(False)
            self.deployed.set_value(True)
        else:
            self.deploying.set_value(True)
            self.deployed.set_value(False)

    def get_wheel_bools(self):
        self.set_wheel_bools()
        return self.deployed.get_value(), self.deploying.get_value()

    def print_wheel_bools(self, position:str):
        if self.deploying.get_value() == True:
            print(f"Wheel in {position} is deploying.")
        if self.deployed.get_value() == True:
            print(f"Wheel in {position} is deployed.")

    def deploy(self):
        self.move_to_target()
        self.set_wheel_bools()

        
    def retract(self):
        self.return_to_zero()
        self.set_wheel_bools()

class LandingGear():
    def __init__(self) -> None:
        self.left = Wheel()
        self.right = Wheel()
        self.front = Wheel()
        self.deploying = BoolAtt(False)
        self.deployed = BoolAtt(False)

    def print_wheel_states(self):
        self.front.print_wheel_bools('Front')
        self.left.print_wheel_bools('Left')
        self.right.print_wheel_bools('Right')
            
    def deploy(self):
        self.left.deploy()
        self.right.deploy()
        self.front.deploy()
    
    def retract(self):
        self.front.retract()
        self.left.retract()
        self.right.retract()
