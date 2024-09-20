from ...GeneralClasses.ControlSurface import ControlSurface


class AirSpike(ControlSurface):
    def __init__(self) -> None:
        super().__init__()
        self.min_position.set(0)
        self.change_rate.set(1)

    def deploy(self):
        if not self.move_to_target():
            return
            #print(f'\n{self.name.get()} is not in tolerance.')

    def retract(self):
        self.return_to_zero()

    def calculate_target(self, delta_p:int):
        tgt_position = self.current_position.get() + delta_p
        self.set_target_position(tgt_position)