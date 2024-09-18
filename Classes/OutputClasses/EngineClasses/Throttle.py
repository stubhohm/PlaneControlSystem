from ...GeneralClasses.ControlSurface import ControlSurface

class Throttle(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set_value(0)
        self.change_rate.set_value(1)

    def deploy(self):
        if not self.move_to_target():
            print(f'{self.name.get_value()} is not in tolerance.')

    def retract(self):
        self.return_to_zero()

    def set_target_position(self, value: int):
        super().set_target_position(value)

