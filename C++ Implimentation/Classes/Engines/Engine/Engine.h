#ifndef ENGINE_H
#define ENGINE_H
#include "AirSpike\AirSpike.h"
#include "Nozzle\Nozzle.h"
#include "Throttle\Throttle.h"

class Engine {

private:
    AirSpike air_spike;
    Nozzle nozzle;
    Throttle throttle;
    bool laterality;
    BoolAttribute is_active;

void name_components();

public:
    
    Engine(bool laterality);

void run();

void activate_engine();

void deactivate_engine();

BoolAttribute get_engine_state();

int get_throttle();

void set_throttle(int new_throttle);

void print(std::string);
};
#endif