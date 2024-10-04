#include "LandingGear.h"

void LandingGear::retract(){
    auto [a, b] = left.retract();
    auto [c ,d] = right.retract();
    auto [e, f] = front.retract();

    if (a || b || c){
        moving.setValue(true);
        retracted.setValue(false);
        deployed.setValue(false);
    } else if (!(d || e || f)){
        retracted.setValue(true);
        moving.setValue(false);
        }
}

void LandingGear::print_wheel_states(){
    front.print_wheel_bools('F');
    left.print_wheel_bools('L');
    right.print_wheel_bools('R');
}

void LandingGear::deploy(){
    auto [a, b] = left.deploy();
    auto [c ,d] = right.deploy();
    auto [e, f] = front.deploy();
    
    if (a || b || c){
        moving.setValue(true);
        retracted.setValue(false);
        deployed.setValue(false);
    } else if (d && e && f){
        deployed.setValue(true);
        moving.setValue(false);
        }
}

void LandingGear::deploy_gear(){
    stow_gear.setValue(false);
}
void LandingGear::retract_gear(){
    stow_gear.setValue(true);
}

BoolAttribute LandingGear::is_deployed(){
    return deployed;
}

BoolAttribute LandingGear::is_stowed(){
    return retracted;
}
void LandingGear::run(){
    if (stow_gear.getValue()){
        retract();
        } else {
        deploy();
        }
}
void LandingGear::engage_brakes(){
    front.engage_brakes();
    left.engage_brakes();
    right.engage_brakes();
}
void LandingGear::release_brakes(){
    front.release_brakes();
    left.release_brakes();
    right.release_brakes();
}
void LandingGear::print(){
    std::cout << "\nMoving:" << moving.getValue() << "\nDeployed: " << deployed.getValue() << "\nRetracted: " << retracted.getValue();
    print_wheel_states();
}