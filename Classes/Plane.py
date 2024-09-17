from .GeneralClasses.Attributes import BoolAtt, IntAtt, StrAtt
from .GeneralClasses.Attributes import Vect2Att, Vect3Att
from .OutputClasses.AirSpikeClasses import AirSpike
from .OutputClasses.ThrottleClasses import Throttle
from .OutputClasses.ControlSurfaceClasses import Elevon
left_outboard = 'LoB'
left_inboard = 'LiB'
right_outboard = 'RoB'
right_inboard = 'RiB'

class Plane ():
    def __init__(self) -> None:
        self.position = Vect3Att()
        self.orientation = Vect3Att()
        self.elevons:dict = {left_outboard : Elevon(left_outboard, )}


