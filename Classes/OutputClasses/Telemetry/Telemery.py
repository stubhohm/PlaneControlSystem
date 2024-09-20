from Modules.Dependencies import math
from ...GeneralClasses.Attributes import Vect3Att, IntAtt

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
        self.orientation.maximum.set(360)
        self.initial_orientation.maximum.set(360)

    def __calculate_velocity(self, speed:int):
        # Get pitch and yaw in radians
        pitch_rad = math.radians(self.orientation.y.get())
        yaw_rad = math.radians(self.orientation.z.get())

        # Calculate velocity components
        vx = speed * math.cos(pitch_rad) * math.cos(yaw_rad)
        vy = speed * math.sin(pitch_rad)
        vz = speed * math.cos(pitch_rad) * math.sin(yaw_rad)
        return (vx, vy, vz)

    def update_telemetry(self, speed:int, orientation:Vect3Att, delta_time:float):
        self.last_position.set(self.position.get())
        self.orientation.set(orientation)
        self.velocity.set(self.__calculate_velocity(speed))
        self.sample_distance.set(self.velocity.scale_vector(delta_time))
        self.position.set(self.position.add_vector(self.sample_distance))
        total_dist = self.total_distance.add(self.sample_distance.get_magnitude())
        self.total_distance.set(total_dist)

    def print(self):
        speed_readout = f"Current speed of {self.velocity.get_magnitude()} m/s."
        distance_readout = f"Current total distance of {self.total_distance.get()} meters."
        heading_readout = f"Roll: {self.orientation.x.get()}, Pitch: {self.orientation.y.get()}, Yaw: {self.orientation.z.get()}"
        position_readout = f"Position x:{self.position.x.get()}, z:{self.position.z.get()}"
        altitude_readout = f"Altitude: {self.position.y.get()}"
        print()
        print(speed_readout)
        print(distance_readout)
        print(heading_readout)
        print(position_readout)
        print(altitude_readout)



