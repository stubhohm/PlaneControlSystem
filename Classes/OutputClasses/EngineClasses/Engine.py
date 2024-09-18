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

    def get_thrust(self):
        l_throttle = self.left_engine.get_throttle()
        r_throttle = self.right_engine.get_throttle()
        return (l_throttle, r_throttle)

    def run(self):
        if not (self.left_engine.get_engine_state() and self.right_engine.get_engine_state()):
            return
        self.left_engine.run()
        self.right_engine.run()
    
    def activate_engines(self):
        self.left_engine.activate_engine()
        self.right_engine.activate_engine()
    
    def deactivate_engines(self):
        self.left_engine.deactivate_engine()
        self.right_engine.deactivate_engine()

    def print(self):
        self.left_engine.print('Left')
        self.right_engine.print('Right')

class Engine():
    def __init__(self, laterality:bool) -> None:
        self.air_spike = AirSpike()
        self.nozzle = Nozzle()
        self.throttle = Throttle()
        self.laterality = laterality
        self.is_active = BoolAtt(False)
        self.__name_components()

    def __name_components(self):
        if self.laterality == left:
            side = 'Left'
        else:
            side = 'Right'
        self.air_spike.name.set_value(f'{side} Air Spike')
        self.throttle.name.set_value(f'{side} Throttle')
        self.nozzle.name.set_value(f'{side} Nozzle')

    def run(self):
        self.air_spike.calculate_target()
        self.nozzle.calculate_target()
        self.throttle.deploy()
        self.air_spike.deploy()
        self.nozzle.deploy()

    def activate_engine(self):
        self.is_active.set_value(True)

    def deactivate_engine(self):
        self.is_active.set_value(False)
    
    def get_engine_state(self):
        return self.is_active.get_value()
    
    def get_throttle(self):
        return self.throttle.current_position.get_value()
    
    def print(self, position):
        throttle = self.get_throttle()
        tgt_throttle = self.throttle.target_position.get_value()
        active = self.get_engine_state()
        air_spike = self.air_spike.current_position.get_value()
        nozzle = self.nozzle.current_position.get_value()
        print()
        print(f'{position} Engine State: {active}')
        print(f'Throttle:{throttle}')
        print(f'Target Throttle:{tgt_throttle}')
        print(f'Airspike Pos {air_spike}')
        print(f'Nozzle Pos {nozzle}')
