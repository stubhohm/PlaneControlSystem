from ...GeneralClasses.ControlSurface import ControlSurface


class AirSpike(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set_value(0)
        self.change_rate.set_value(1)

    def deploy(self):
        self.move_to_target()

    def retract(self):
        self.return_to_zero()

    def calculate_target(self):
        pass