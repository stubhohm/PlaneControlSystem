from .GeneralClasses.Attributes import BoolAtt, StrAtt
from .GeneralClasses.Attributes import Vect3Att
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
        self.elevons.set_trim(trim)
        self.rudders.set_trim(trim)

    def __set_thrust(self, thrust:int):
        self.engines.set_thrust(thrust)
    
    def __set_control_surfaces(self, control_input:Vect3Att):
        self.elevons.set_positions(control_input)
        self.rudders.set_positions(control_input)

    def __set_SAS(self, stability_assistance:bool):
        self.stability_assistance.set(stability_assistance)

    def startup_sequence(self):
        self.engines.activate_engines()
        self.landing_gear.deploy_gear()
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
        ## For testing
        self.telemetry.orientation.set(control_vector)

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
        
        self.telemetry.update_telemetry(speed, self.telemetry.orientation.get(), .1)


