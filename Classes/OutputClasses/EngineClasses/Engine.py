from ....Keys.Keys import left, right
from .AirSpike import AirSpike
from .Nozzle import Nozzle
from .Throttle import Throttle

class Engines():
    def __init__(self) -> None:
        self.left_engine = Engine(left)
        self.right_engine = Engine(right)

    def set_thrust(self, thrust:int):
        self.left_engine.throttle.set_target_position(thrust)
        self.right_engine.throttle.set_target_position(thrust)


class Engine():
    def __init__(self, laterality:bool) -> None:
        self.air_spike = AirSpike()
        self.nozzle = Nozzle()
        self.throttle = Throttle()
        self.laterality = laterality
