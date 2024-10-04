#include "Wheel.h"

    Wheel::Wheel(){
        min_position.setValue(0);
        change_rate.setValue(5);
        target_tolerance.setValue(2);
        set_target_position(max_position.getValue());
        deploying.setValue(false);
        deployed.setValue(false);
        brakes_engaged.setValue(false);
}

void Wheel::engage_brakes(){
        brakes_engaged.setValue(true);
}

void Wheel::release_brakes(){
        brakes_engaged.setValue(false);
}

void Wheel::get_brake_state(){
        brakes_engaged.getValue();
}

void Wheel::set_wheel_bools(){
        // Assume we are retracted
        deployed.setValue(false);
        if (current_position.getValue() == target_position.getValue()){
            // It is not moving
            deploying.setValue(false);
            } else {
            deploying.setValue(true);
            }
        if (current_position.getValue() == max_position.getValue()){
            // It is depoloyed
            deployed.setValue(true);
        }
}

std::tuple<bool, bool> Wheel::get_wheel_bools(){
        set_wheel_bools();
        return std::make_tuple(deploying.getValue(), deployed.getValue());
}

void Wheel::print_wheel_bools(char position){
        auto [a, b] = get_wheel_bools();
        deploying.setValue(a);
        deployed.setValue(b);
        if (deploying.getValue()){
            std::cout <<"Wheel on {position} is moving.";
            std::cout << "Ammount: {self.current_position.get()}";
            }
        if (deployed.getValue()){
            std::cout << "Wheel on {position} is deployed.";
            }
        if (brakes_engaged.getValue()){
            std::cout <<"Wheel on {position} is braking.";
            }
        if (deployed.getNotValue() && deploying.getNotValue()){
            std::cout << "Wheel on {position} is retracted.";
            }
        std::cout << current_position.getValue();
        std::cout << target_position.getValue();
}

std::tuple<bool, bool> Wheel::deploy(){
        set_target_position(max_position.getValue());
        run();
        //#f'\n{self.name.get()} is not in tolerance.')
        return get_wheel_bools();
}  

std::tuple<bool, bool> Wheel::retract(){
        return_to_zero();
        run();
        return get_wheel_bools();
}

void Wheel::run(){
        move_to_target();
}
