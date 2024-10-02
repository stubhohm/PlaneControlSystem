#ifndef ELEVONS_H
#define ELEVONS_H
#include "Elevon\Elevon.h"

class Elevons{
private:
    Elevon left_inboard, left_outboard, right_inboard, right_ourboard;

    Elevons();

void bind_target_position();

void bind_trim();

bool is_in_tolerance(bool include_trim);

void incriment_position();

void incriment_trim();

public:

bool return_to_zero();

bool move_to_target();

void set_target_position(int target_value);

void set_target_trim(int target_value);

};

#endif