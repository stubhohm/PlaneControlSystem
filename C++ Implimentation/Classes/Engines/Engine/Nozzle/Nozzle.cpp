#include "Nozzle.h"

    Nozzle::Nozzle()
    : barometer() 
    {
    min_position.setValue(0);
    change_rate.setValue(1);
    }

void Nozzle::calculate_target(){
    int tgt_position = current_position.getValue() + barometer.getValue();
    set_target_position(tgt_position);
}

void Nozzle::deploy(){
    if (move_to_target().getNotValue()){
        return;
        //#print(f'\n{self.name.get()} is not in tolerance.')
        }
}

void Nozzle::retract(){
    return_to_zero();
}

void Nozzle::run(){
    calculate_target();
    deploy();
}
