#ifndef WHEEL_H
#define WHEEL_H
#include "ControlSurface.h"
#include "BoolAttribute.h"
#include "..\Modules\Dependencies.h"


class Wheel : public ControlSurface{
 
private:
    BoolAttribute deploying, deployed, brakes_engaged;

public:
    Wheel();

void engage_brakes();

void release_brakes();

void get_brake_state();

void set_wheel_bools();

std::tuple<bool, bool> get_wheel_bools();

void print_wheel_bools(char position);

std::tuple<bool, bool> deploy();

std::tuple<bool, bool> retract();

void run();
};

#endif