#ifndef TELEMETRY_H
#define TELEMETRY_H

#include "..\Attributes\IntAtt\IntAttribute.h"
#include "..\Attributes\V3Att\V3Attribute.h"

class Telemetry{
private :
    V3Attribute last_position, position, initial_position, initial_orientation, velocity, sample_distance;
    IntAttribute speed, total_distance;

void set_telemetry_bounds();

V3Attribute calculate_velocity(int current_speed);

public:

    V3Attribute orientation;

    Telemetry();

void update_telemetry(int current_speed, V3Attribute orientation, float delta_time);

void print();
};
#endif