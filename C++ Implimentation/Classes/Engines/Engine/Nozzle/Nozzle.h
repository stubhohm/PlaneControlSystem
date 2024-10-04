#ifndef NOZZLE_H
#define NOZZLE_H
#include "..\ControlSurface\ControlSurface.h"
#include "..\Sensor\Barometer\Barometer.h"

class Nozzle : public ControlSurface {

private:

    Barometer barometer;

void calculate_target();

void deploy();

void retract();

public:

    Nozzle();

void run();
};
#endif