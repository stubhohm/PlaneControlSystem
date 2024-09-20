from ...GeneralClasses.ControlSurface import ControlSurface

class Nozzle(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set(0)
        self.change_rate.set(1)

    def deploy(self):
        if not self.move_to_target():
<<<<<<< HEAD
            print(f'{self.name.get()} is not in tolerance.')
=======
            return
            #print(f'\n{self.name.get()} is not in tolerance.')
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153

    def retract(self):
        self.return_to_zero()

    def calculate_target(self, delta_p:int):
        tgt_position = self.current_position.get() + delta_p
        self.set_target_position(tgt_position)