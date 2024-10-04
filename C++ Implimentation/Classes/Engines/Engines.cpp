#include "Engines.h"

Engines::Engines()
  : left_engine(left),
    right_engine(right)
    {}

void Engines::set_thrust(int thrust){
    left_engine.set_throttle(thrust);
    right_engine.set_throttle(thrust);
}

std::pair<int, int> Engines::get_thrust(){
    int l_throttle = left_engine.get_throttle();
    int r_throttle = right_engine.get_throttle();
    return std::make_pair(l_throttle, r_throttle);
}

void Engines::run(){
    if (left_engine.get_engine_state().getNotValue() && right_engine.get_engine_state().getNotValue()){
        return;
        }
    left_engine.run();
    right_engine.run();
}

void Engines::activate_engines(){
    left_engine.activate_engine();
    right_engine.activate_engine();
}

void Engines::deactivate_engines(){
    left_engine.deactivate_engine();
    right_engine.deactivate_engine();
}

void Engines::print(){
    std::string left_side = "Left";
    std::string right_side = "Right";
    left_engine.print(left_side);
    right_engine.print(right_side);
}