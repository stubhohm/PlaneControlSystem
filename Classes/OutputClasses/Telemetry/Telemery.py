from Modules.Dependencies import cosine_lookup, sine_lookup
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
        self.orientation.maximum.set(360)
        self.initial_orientation.maximum.set(360)

    def __calculate_velocity(self, speed:int):
        pitch = self.orientation.y.get()
        yaw = self.orientation.z.get()
    
        vx = speed * cosine_lookup(pitch) * cosine_lookup(yaw)
        vy = speed * cosine_lookup(pitch) * sine_lookup(yaw)
        vz = speed * sine_lookup(pitch)
        print(vx, vy, vz)
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
        speed_readout = f"Spd: {self.velocity.get_magnitude()} m/s."
        distance_readout = f"Tot dist: {self.total_distance.get()} meters."
        heading_readout = f"P: {self.orientation.y.get()}, R: {self.orientation.x.get()}, Y: {self.orientation.z.get()}"
        position_readout = f"Pos x:{self.position.x.get()}, z:{self.position.z.get()}"
        altitude_readout = f"Alt: {self.position.y.get()}"
        print(speed_readout)
        print(distance_readout)
        print(heading_readout)
        print(position_readout)
        print(altitude_readout)



