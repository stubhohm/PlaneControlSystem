#include "Throttle.h"

    Throttle::Throttle() {
    min_position.setValue(0);
    change_rate.setValue(1);
}

int Throttle::get_current_position(){
    return current_position.getValue();
}

void Throttle::deploy(){
    if (move_to_target().getNotValue()){
        return;
        //#print(f'\n{self.name.get()} is not in tolerance.')
        }
}

void Throttle::retract(){
    return_to_zero();
}

void Throttle::run(){
    deploy();
}
