#ifndef ELEVON_H
#define ELEVON_H
#include "..\Attributes\BoolAtt\BoolAttribute.h"
#include "..\Attributes\StrAtt\CharAttribute.h"
#include "..\ControlSurface\ControlSurface.h"

class Elevon : public ControlSurface{

private: 
    
    CharAttribute name;
    BoolAttribute laterality, proximal;

int set_yaw(int yaw, bool btrim);

int set_pitch(int pitch, bool btrim);

int set_roll(int roll, bool btrim);

public:

    Elevon(char* new_name, bool new_laterality, bool new_proximal);

void deploy();

void retract();

void set_position(int roll, int pitch, int yaw, bool btrim);

void print();
};

#endif