#include "Telemetry.h"

Telemetry::Telemetry()
  : speed(0),
    total_distance(0)
    {}

void Telemetry::set_telemetry_bounds(){
    orientation.set_maximum(360);
    orientation.set_minimum(0);
    initial_orientation.set_minimum(360);
    initial_orientation.set_minimum(0);
}

V3Attribute Telemetry::calculate_velocity(int current_speed){
    // Get pitch and yaw in deg
    int pitch_rad = orientation.getY();
    int yaw_rad = orientation.getZ();

    // Calculate velocity components
    int vx = current_speed * cosine_lookup(pitch_rad) * cosine_lookup(yaw_rad);
    int vy = current_speed * sine_lookup(pitch_rad);
    int vz = current_speed * cosine_lookup(pitch_rad) * sine_lookup(yaw_rad);
    V3Attribute velocity_vector;
    velocity_vector.setValue(vx, vy, vz);
    return velocity_vector;
}

void Telemetry::update_telemetry(int current_speed, V3Attribute orientation, float delta_time)
{
    last_position.setValue(position.getValue());
    orientation.setValue(orientation);
    velocity.setValue(calculate_velocity(current_speed));
    sample_distance.setValue(velocity.scale_vector(delta_time));
    position.setValue(position.add(sample_distance));
    int time_step_distance = total_distance.add(sample_distance.get_magnitude());
    total_distance.setValue(time_step_distance);
}

void Telemetry::print(){
    std::string speed_readout = "Current speed of {velocity.get_magnitude()} m/s.";
    std::string distance_readout = "Current total distance of {total_distance.getValue()} meters.";
    std::string heading_readout = "Roll: {orientation.x.getValue()}, Pitch: {orientation.y.getValue()}, Yaw: {orientation.z.getValue()}";
    std::string position_readout = "Position x:{position.x.getValue()}, z:{position.z.getValue()}";
    std::string altitude_readout = "Altitude: {position.y.getValue()}";
    std::cout << std::endl;
    std::cout<< speed_readout << std::endl;
    std::cout<< distance_readout << std::endl;
    std::cout<< heading_readout << std::endl;
    std::cout<< position_readout << std::endl;
    std::cout<< altitude_readout << std::endl;
}


