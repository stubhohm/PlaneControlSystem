#ifndef THROTTLE_H
#define THROTTLE_H
#include "..\ControlSurface\ControlSurface.h"

class Throttle : public ControlSurface {

private:

void deploy();

void retract();

public:

    Throttle();

void run();

};
#endif