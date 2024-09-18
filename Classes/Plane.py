from Keys.Keys import left, right, proximal, distal
from .GeneralClasses.Attributes import BoolAtt, IntAtt, StrAtt
from .GeneralClasses.Attributes import Vect2Att, Vect3Att
from .OutputClasses.EngineClasses.Engine import Engines
from .OutputClasses.ControlSurfaceClasses.Elevon import Elevons
from .OutputClasses.ControlSurfaceClasses.Rudder import Rudders
from .OutputClasses.ControlSurfaceClasses.LandingGear import LandingGear
from .OutputClasses.Telemetry.Telemery import Telemetry

class Plane ():
    def __init__(self, name) -> None:
        self.name = StrAtt(name)
        self.telemetry = Telemetry()
        self.elevons = Elevons() 
        self.rudders = Rudders() 
        self.engines = Engines()
        self.landing_gear = LandingGear()
        self.stability_assistance = BoolAtt(False)
        
    def get_coordinates(self):
        print('not impliments')

    def __set_trim(self, trim:Vect3Att):
        roll = trim.x.get_value()
        ptich = trim.y.get_value()
        yaw = trim.z.get_value()

    def __set_thrust(self, thrust:int):
        self.engines.set_thrust(thrust)
    
    def __set_control_surfaces(self, control_input:Vect3Att):
        roll = control_input.x.get_value()
        pitch = control_input.y.get_value()
        yaw = control_input.z.get_value()
        self.telemetry.orientation.set_value(control_input)

    def __set_SAS(self, stability_assistance:bool):
        self.stability_assistance.set_value(stability_assistance)

    def startup_sequence(self):
        self.engines.activate_engines()
        self.landing_gear.deploy()
        self.landing_gear.engage_brakes()
        self.elevons.return_to_zero()

    def print(self):
        self.telemetry.print()
        self.elevons.print()
        self.rudders.print()
        self.landing_gear.print()
        self.engines.print()

    def impliment_control_inputs(self, SAS_toggle:bool, thrust:int, trim_vector:Vect3Att, control_vector:Vect3Att):
        self.__set_SAS(SAS_toggle)
        self.__set_thrust(thrust)
        self.__set_trim(trim_vector)
        self.__set_control_surfaces(control_vector)

    def run(self):
        self.engines.run()
        self.elevons.run()
        self.rudders.run()
        self.landing_gear.run()

    def set_telemetry(self):

        max_speed = 30
        thrust = self.engines.get_thrust()
        avg_thrust = int ((thrust[0] + thrust[1])/2)
        speed = int(max_speed * (avg_thrust / 100))
        
        self.telemetry.update_telemetry(speed, self.telemetry.orientation.get_value(), .1)


