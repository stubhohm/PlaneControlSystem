from Keys.Keys import left, right
from ...GeneralClasses.Attributes import BoolAtt
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

    def run_engine(self):
        if not (self.left_engine.is_active.get_value() and self.right_engine.is_active.get_value()):
            return
        self.left_engine.run_engine()
        self.right_engine.run_engine()
    
    def activate_engines(self):
        self.left_engine.activate_engine()
        self.right_engine.activate_engine()
    
    def deactivate_engines(self):
        self.left_engine.deactivate_engine()
        self.right_engine.deactivate_engine()



class Engine():
    def __init__(self, laterality:bool) -> None:
        self.air_spike = AirSpike()
        self.nozzle = Nozzle()
        self.throttle = Throttle()
        self.laterality = laterality
        self.is_active = BoolAtt(False)

    def run_engine(self):
        self.air_spike.calculate_target()
        self.nozzle.calculate_target()
        self.throttle.move_to_target()

    def activate_engine(self):
        self.is_active.set_value(True)

    def deactivate_engine(self):
        self.is_active.set_value(False)
    
    def get_engine_state(self):
        return self.is_active.get_value()
