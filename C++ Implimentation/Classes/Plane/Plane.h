#ifndef PLANE_H
# define PLANE_H
#include "..\Engines\Engines.h"
#include "..\Elevons\Elevons.h"
#include "..\Rudders\Rudders.h"
#include "..\LandingGear\LandingGear.h"
#include "..\Telemetry\Telemetry.h"

class Plane{
private:

void set_trim(V3Attribute trim_vector);

void set_thrust(int thrust);

void set_control_surfaces(V3Attribute control_input);

void set_SAS(bool new_sas_status);

public:

    CharAttribute name;
    Telemetry telemetry;
    Elevons elevons;
    Rudders rudders;
    Engines engines;
    LandingGear landing_gear;
    BoolAttribute stability_assistance;

Plane(std::string new_name);
   
void get_coordinates();

void startup_sequence();

void print();

void impliment_control_inputs(bool SAS_toggle, int thrust,V3Attribute trim_vector,V3Attribute control_vector);

void run();

void set_telemetry();
};
#endif
