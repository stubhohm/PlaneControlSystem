#include "Plane.h"


Plane::Plane(std::string new_name){
    name.setValue(new_name);
    stability_assistance.setValue(false);
}

void Plane::set_trim(V3Attribute trim_vector){
    elevons.set_trim(trim_vector);
    rudders.set_trim(trim_vector);
}

void Plane::set_thrust(int thrust){
    engines.set_thrust(thrust);
}

void Plane::set_control_surfaces(V3Attribute control_input){
    elevons.set_positions(control_input);
    rudders.set_positions(control_input);
}

void Plane::set_SAS(bool new_sas_status){
    stability_assistance.setValue(new_sas_status);
}

void Plane::get_coordinates(){
    std::cout << "not impliments" << std::endl;
}

void Plane::startup_sequence(){
    engines.activate_engines();
    landing_gear.deploy_gear();
    landing_gear.engage_brakes();
    elevons.return_to_zero();
}
void Plane::print(){
    telemetry.print();
    elevons.print();
    rudders.print();
    landing_gear.print();
    engines.print();
}

void Plane::impliment_control_inputs(bool SAS_toggle, int thrust,V3Attribute trim_vector,V3Attribute control_vector){
    set_SAS(SAS_toggle);
    set_thrust(thrust);
    set_trim(trim_vector);
    set_control_surfaces(control_vector);
    // For testing
    telemetry.orientation.setValue(control_vector);
}

void Plane::run(){
    engines.run();
    elevons.run();
    rudders.run();
    landing_gear.run();
}

void Plane::set_telemetry(){
    int max_speed = 30;
    
    auto thrust = engines.get_thrust();
    int avg_thrust = int ((thrust.first + thrust.second) >> 1);
    int speed = int(max_speed * (avg_thrust / 100));
    
    telemetry.update_telemetry(speed, telemetry.orientation.getValue(), .1);
}