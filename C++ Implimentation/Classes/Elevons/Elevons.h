#ifndef ELEVONS_H
#define ELEVONS_H
#include "Elevon\Elevon.h"
#include "V3Attribute.h"

class Elevons{
private:
    Elevon left_inboard, left_outboard, right_inboard, right_outboard;

    Elevons();

void set_position(int roll, int pitch, int yaw, bool btrim){}

public:

void set_positions(V3Attribute vector, bool btrim){}
void set_trim(V3Attribute control_input){}
void run(){}
void return_to_zero(){}
void  print(){}

};

#endif