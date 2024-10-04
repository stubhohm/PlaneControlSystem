#include "Elevons.h"

    Elevons::Elevons()
      : left_inboard("l", left, proximal),
        right_inboard("r", right, proximal),
        left_outboard("L", left, distal),
        right_outboard("R", right, distal)
    {}

void Elevons::set_position(int roll, int pitch, int yaw, bool btrim){
        left_inboard.set_position(roll, pitch, yaw, btrim);
        left_outboard.set_position(roll, pitch, yaw, btrim);
        right_inboard.set_position(roll, pitch, yaw, btrim);
        right_outboard.set_position(roll, pitch, yaw, btrim);
}
void Elevons::set_positions(V3Attribute vector, bool btrim = false){
        int roll = vector.getX();
        int pitch = vector.getY();
        int yaw = vector.getZ();
        set_position(roll, pitch, yaw, btrim);
}
void Elevons::set_trim(V3Attribute control_input){
        bool btrim =true;
        set_positions(control_input, btrim);
}
void Elevons::run(){
        left_inboard.deploy();
        left_outboard.deploy();
        right_inboard.deploy();
        right_outboard.deploy();
}
void Elevons::return_to_zero(){
        left_inboard.return_to_zero();
        left_outboard.return_to_zero();
        right_inboard.return_to_zero();
        right_outboard.return_to_zero();
}
void  Elevons::print(){
        left_inboard.print();
        left_outboard.print();
        right_inboard.print();
        right_outboard.print();
}
