#include "AirSpike.h"

    AirSpike::AirSpike()
    : barometer() 
    {
    min_position.setValue(0);
    change_rate.setValue(1);
    }

void AirSpike::calculate_target(){
    int tgt_position = current_position.getValue() + barometer.getValue();
    set_target_position(tgt_position);
}

void AirSpike::deploy(){
    if (move_to_target().getNotValue()){
        return;
        //#print(f'\n{self.name.get()} is not in tolerance.')
        }
}

void AirSpike::retract(){
    return_to_zero();
}

void AirSpike::run(){
    calculate_target();
    deploy();
}
