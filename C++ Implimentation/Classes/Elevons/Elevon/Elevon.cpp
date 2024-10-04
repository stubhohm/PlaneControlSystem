#include "Elevon.h"


    Elevon::Elevon(char* new_name, bool new_laterality, bool new_proximal) 
        : name(new_name), laterality(new_laterality), proximal(new_proximal) {}

int Elevon::set_yaw(int yaw, bool btrim){
        return 0;
}

int Elevon::set_pitch(int pitch, bool btrim){
        int pitch = 0;
        if (proximal.getValue()){
            pitch = int(pitch / 2);
        }
        if (btrim){
            pitch = int(pitch / 2);
            return pitch;
        } else {
            return pitch;
        }
}
int Elevon::set_roll(int roll, bool btrim){
        if (laterality.getValue()){
            roll *= -1;
        }
        if (proximal.getValue()){
            roll = int(roll / 2);
        }
        if (btrim){
            return roll;
        } else {
            return roll;
        }
}


void Elevon::retract(){
        return_to_zero();
}

void Elevon::deploy(){
        if (move_to_target().getNotValue()){
            return;
        }
        std::cout << "\n" << name.getValue() << "is not in tolerance.";
}

void Elevon::set_position(int roll, int pitch, int yaw, bool btrim){
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

void Elevon::print(){
        std::cout << "\n" << name.getValue();
        std::cout << "\nCurrent: " << current_position.getValue();
        std::cout << "\nTarget: " <<target_position.getValue();
}
