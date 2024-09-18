from ..GeneralClasses.Attributes import Vect3Att
from .FlightAssistant import FlightAssistant
from .LandingGear import LandingGear
from .TargetOrientation import TargetOrientation
from .TargetThrottle import TargetThrottle
from .TargetTrim import TargetTrim


class Controller():
    def __init__(self) -> None:
        self.flight_assistant = FlightAssistant()
        self.landing_gear = LandingGear()
        self.target_orientation = TargetOrientation()
        self.target_trim = TargetTrim()
        self.target_throttle = TargetThrottle()

    def __set_trottle(self, value:int):
        self.target_throttle.throttle.set_value(value)

    def __set_flight_assistant(self, value:bool):
        self.flight_assistant.set_deployed.set_value(value)

    def __set_landing_gear(self, value:bool):
        self.landing_gear.set_deployed.set_value(value)

    def __set_target_orientation(self, value:Vect3Att):
        self.target_orientation.vector.set_value(value)

    def __set_target_trim(self, value:Vect3Att):
        self.target_trim.vector.set_value(value)

    def set_values(self, throttle:int, flight_assist:bool, landing_gear:bool, tgt_orient:Vect3Att, tgt_trim:Vect3Att):
        self.__set_flight_assistant(flight_assist)
        self.__set_landing_gear(landing_gear)
        self.__set_target_orientation(tgt_orient)
        self.__set_target_trim(tgt_trim)
        self.__set_trottle(throttle)
