from ....Modules.Dependencies import math
from ...GeneralClasses.Attributes import Vect3Att, BoolAtt, IntAtt

class Telemetry():
    def __init__(self) -> None:
        self.last_position = Vect3Att()
        self.position = Vect3Att()
        self.initial_position = Vect3Att()
        self.orientation = Vect3Att()
        self.initial_orientation = Vect3Att()
        self.velocity = Vect3Att()
        self.speed = IntAtt(0)
        self.total_distance = IntAtt(0)
        self.sample_distance = Vect3Att()
        self.__set_telemetry_bounds()

    def __set_telemetry_bounds(self):
        self.orientation.maximum.set_value(360)
        self.initial_orientation.maximum.set_value(360)

    def __calculate_velocity(self, speed:int):
        pitch_rad = math.radians(self.orientation.y.get_value())
        yaw_rad = math.radians(self.orientation.z.get_value())
    
        vx = speed * math.cos(pitch_rad) * math.cos(yaw_rad)
        vy = speed * math.cos(pitch_rad) * math.sin(yaw_rad)
        vz = speed * math.sin(pitch_rad)
        return (vx, vy, vz)

    def update_telemetry(self, speed:int, orientation:Vect3Att, delta_time:float):
        self.last_position.set_value(self.position.get_value())
        self.orientation.set_value(orientation)
        self.velocity.set_value(self.__calculate_velocity(speed))
        self.sample_distance.set_value(self.velocity.scale_vector(delta_time))
        self.position.set_value(self.position.add_vector(self.sample_distance))
        total_dist = self.total_distance.add(self.sample_distance.get_magnitude())
        self.total_distance.set_value(total_dist)



