from ...GeneralClasses.ControlSurface import ControlSurface
from ...GeneralClasses.Attributes import BoolAtt

class Wheel(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set(0)
<<<<<<< HEAD
        self.change_rate.set(1)
=======
        self.change_rate.set(5)
        self.target_tolerance.set(2)
        self.set_target_position(self.max_position.get())
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153
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
<<<<<<< HEAD
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
        if self.deploying.get() == True:
            print(f"Wheel in {position} is deploying.")
        if self.deployed.get() == True:
            print(f"Wheel in {position} is deployed.")
        if self.brakes_engaged.get == True:
            print(f"Wheel in {position} is braking.")

    def deploy(self):
        if not self.move_to_target():
            print(f'{self.name.get()} is not in tolerance.')
        self.set_wheel_bools()
=======
        # Assume we are retracted
        self.deployed.set(False)
        if self.current_position.get() == self.target_position.get():
            # It is not moving
            self.deploying.set(False)
        else:
            self.deploying.set(True)
        if self.current_position.get() == self.max_position.get():
            # It is depoloyed
            self.deployed.set(True)

    def get_wheel_bools(self):
        self.set_wheel_bools()
        return  self.deploying.get(), self.deployed.get()

    def print_wheel_bools(self, position:str):
        deploying, deployed = self.get_wheel_bools()
        if deploying:
            print(f"Wheel on {position} is moving.")
            print(f"Ammount: {self.current_position.get()}")
        if deployed:
            print(f"Wheel on {position} is deployed.")
        if self.brakes_engaged.get():
            print(f"Wheel on {position} is braking.")
        if not deployed and not deploying:
            print(f"Wheel on {position} is retracted.")
        print(self.current_position.get())
        print(self.target_position.get())

    def deploy(self):
        self.set_target_position(self.max_position.get())
        self.run()
            #print(f'\n{self.name.get()} is not in tolerance.')
        return self.get_wheel_bools()
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153
     
    def retract(self):
        self.return_to_zero()
        self.run()
        return self.get_wheel_bools()
    
    def run(self):
        self.move_to_target()


class LandingGear():
    def __init__(self) -> None:
        self.__left = Wheel()
        self.__right = Wheel()
        self.__front = Wheel()
        self.__moving = BoolAtt(False)
        self.__deployed = BoolAtt(False)
        self.__retracted = BoolAtt(False)
        self.__stow_gear = BoolAtt(False)

    def deploy_gear(self):
        self.__stow_gear.set(False)

    def retract_gear(self):
        self.__stow_gear.set(True)

    def is_deployed(self):
        return self.__deployed.get()
    
    def is_stowed(self):
        return self.__retracted.get()

    def run(self):
        if self.__stow_gear.get():
            self.__retract()
        else:
            self.__deploy()

    def __print_wheel_states(self):
        self.__front.print_wheel_bools('Front')
        self.__left.print_wheel_bools('Left')
        self.__right.print_wheel_bools('Right')
            
    def __deploy(self):
        a, d = self.__left.deploy()
        b, e = self.__right.deploy()
        c, f = self.__front.deploy()
        if True in [a, b, c]:
            self.__moving.set(True)
            self.__retracted.set(False)
            self.__deployed.set(False)
        elif False not in [d, e, f]:
            self.__deployed.set(True)
            self.__moving.set(False)
    
    def __retract(self):
        a, d = self.__left.retract()
        b, e = self.__right.retract()
        c, f = self.__front.retract()
        if True in [a, b, c]:
            self.__moving.set(True)
            self.__retracted.set(False)
            self.__deployed.set(False)
        elif True not in [d, e, f]:
            self.__retracted.set(True)
            self.__moving.set(False)

    def engage_brakes(self):
        self.__front.engage_brakes()
        self.__left.engage_brakes()
        self.__right.engage_brakes()

    def release_brakes(self):
        self.__front.release_brakes()
        self.__left.release_brakes()
        self.__right.release_brakes()

    def print(self):
        print(f'\nMoving: {self.__moving.get()} \nDeployed: {self.__deployed.get()} \nRetracted: {self.__retracted.get()}')
        self.__print_wheel_states()
