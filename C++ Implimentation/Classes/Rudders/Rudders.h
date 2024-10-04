#ifndef RUDDERS_H
#define RUDDERS_H
#include "Rudder\Rudder.h"
#include "V3Attribute.h"
#include "Keys.h"

class Rudders{
private:
    Rudder left_rudder, right_rudder;

void set_position(int roll, int pitch, int yaw, bool btrim){}

public:

    Rudders();

void set_positions(V3Attribute vector, bool btrim = false){}
void set_trim(V3Attribute control_input){}
void run(){}
void return_to_zero(){}
void  print(){}

};

#endif