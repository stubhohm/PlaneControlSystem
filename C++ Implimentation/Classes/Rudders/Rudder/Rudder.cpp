#include "Rudder.h"

    Rudder::Rudder(char* new_name, bool new_laterality) 
        : name(new_name), laterality(new_laterality) {}

int Rudder::set_yaw(int yaw, bool btrim){
        if (btrim){
            int yaw = int(yaw / 2);
            }
        return yaw;
}

int Rudder::set_pitch(int pitch, bool btrim){
        if (laterality.getValue() == left){
            pitch *= -1;
            }
        if (btrim){
            pitch = int(pitch / 2);
            return pitch;
        } else {
            return pitch;
            }
}
int Rudder::set_roll(int roll, bool btrim){
        return 0;
}


void Rudder::retract(){
        return_to_zero();
}

void Rudder::deploy(){
        if (move_to_target().getNotValue()){
            return;
        }
        std::cout << "\n" << name.getValue() << "is not in tolerance.";
}

void Rudder::set_position(int roll, int pitch, int yaw, bool btrim){
        int r = set_roll(roll, btrim);
        int p = set_pitch(pitch, btrim);
        int y = set_yaw(yaw, btrim);
        int summation = int(r + p + y);
        if (btrim){
            set_target_trim(summation);
        } else {
            set_target_position(summation);
        }
}

void Rudder::print(){
        std::cout << "\n" << name.getValue();
        std::cout << "\nCurrent: " << current_position.getValue();
        std::cout << "\nTarget: " <<target_position.getValue();
}
