#ifndef ENGINES_H
#define ENGINES_H
#include "Engine\Engine.h"

class Engines {

private:


public:

    Engine left_engine, right_engine;

    Engines();

void set_thrust(int thrust);

std::pair<int, int> get_thrust();

void run();

void activate_engines();

void deactivate_engines();

void print();
};
#endif