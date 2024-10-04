#ifndef RUDDER_H
#define RUDDER_H
#include "..\Attributes\BoolAtt\BoolAttribute.h"
#include "..\Attributes\StrAtt\CharAttribute.h"
#include "..\ControlSurface\ControlSurface.h"
#include "..\Modules\Dependencies.h"

class Rudder : public ControlSurface{

private: 
    
    CharAttribute name;
    BoolAttribute laterality;

int set_yaw(int yaw, bool btrim);

int set_pitch(int pitch, bool btrim);

int set_roll(int roll, bool btrim);

public:

    Rudder(char* new_name, bool new_laterality);

void deploy();

void retract();

void set_position(int roll, int pitch, int yaw, bool btrim);

void print();
};

#endif