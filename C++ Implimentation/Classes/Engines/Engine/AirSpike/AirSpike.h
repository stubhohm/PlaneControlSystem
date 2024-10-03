#ifndef AIRSPIKE_H
#define AIRSPIKE_H
#include "..\Attributes\IntAtt\IntAttribute.h"
#include "..\Attributes\StrAtt\CharAttribute.h"
#include "..\Attributes\BoolAtt\BoolAttribute.h"

class ControlSurface{
private:
    IntAttribute starting_position, current_position, target_position, max_position, min_position, trim, target_trim, change_rate, target_tolerance;
    CharAttribute name;

    ControlSurface();

void bind_target_position();

void bind_trim();

BoolAttribute is_in_tolerance(bool include_trim);

void incriment_position();

void incriment_trim();

public:

BoolAttribute return_to_zero();

BoolAttribute move_to_target();

void set_target_position(int target_value);

void set_target_trim(int target_value);

};

#endif