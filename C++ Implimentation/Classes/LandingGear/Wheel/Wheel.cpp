#include "Wheel.h"
#include <iostream>
#include <tuple>

    Wheel(){
        min_position.setValue(0);
        change_rate.setValue(5);
        target_tolerance.setValue(2);
        set_target_position(max_position.getValue());
        deploying.setValue(false);
        deployed.setValue(false);
        brakes_engaged.setValue(false);
}

void engage_brakes(){
        brakes_engaged.setValue(true);
}

void release_brakes(){
        brakes_engaged.setValue(false);
}

void get_brake_state(){
        brakes_engaged.getValue();
}

void set_wheel_bools(){
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

std::tuple<bool, bool> get_wheel_bools(){
        set_wheel_bools();
        return std::make_tuple(deploying.getValue(), deployed.getValue());
}

void print_wheel_bools(char position){
        auto result = get_wheel_bools();
        deploying.setValue(std::get<0>(result));
        deployed.setValue(std::get<1>(result));
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
        if (deployed.getNotValue() and deploying.getNotValue()){
            std::cout << "Wheel on {position} is retracted.";
            }
        std::cout << current_position.getValue();
        std::cout << target_position.getValue();
}

std::tuple<bool, bool> deploy(){
        set_target_position(max_position.getValue());
        run();
        //#f'\n{self.name.get()} is not in tolerance.')
        return self.get_wheel_bools();
}  

std::tuple<bool, bool> retract(){
        return_to_zero();
        run();
        return get_wheel_bools();
}

void run(self){
        self.move_to_target()
}