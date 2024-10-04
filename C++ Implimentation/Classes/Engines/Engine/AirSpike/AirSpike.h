#ifndef AIRSPIKE_H
#define AIRSPIKE_H
#include "..\ControlSurface\ControlSurface.h"
#include "..\Sensor\Barometer\Barometer.h"
#include "..\Modules\Dependencies.h"

class AirSpike : public ControlSurface {

private:

    Barometer barometer;

void calculate_target();

void deploy();

void retract();

public:

    AirSpike();

void run();
};
#endif