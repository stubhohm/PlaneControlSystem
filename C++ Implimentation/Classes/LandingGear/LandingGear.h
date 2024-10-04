#ifndef LANDING_GEAR_H
# define LANDING_GEAR_H

#include "..\Modules\Dependencies.h"
#include "BoolAttribute.h"
#include "Wheel\Wheel.h"


class LandingGear{
private: 
    Wheel left, right, front;
    BoolAttribute moving, deployed, retracted, stow_gear;

void retract();

void print_wheel_states();

void deploy();

public:

void deploy_gear();

void retract_gear();

BoolAttribute is_deployed();

BoolAttribute is_stowed();

void run();

void engage_brakes();

void release_brakes();

void print();
};

#endif