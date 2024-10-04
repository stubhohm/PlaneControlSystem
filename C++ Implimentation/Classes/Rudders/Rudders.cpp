#include "Rudders.h"

    Rudders::Rudders()
      : left_rudder("l", left),
        right_rudder("r", right)
    {}

void Rudders::set_position(int roll, int pitch, int yaw, bool btrim){
        left_rudder.set_position(roll, pitch, yaw, btrim);
        right_rudder.set_position(roll, pitch, yaw, btrim);
}
void Rudders::set_positions(V3Attribute vector, bool btrim = false){
        int roll = vector.getX();
        int pitch = vector.getY();
        int yaw = vector.getZ();
        set_position(roll, pitch, yaw, btrim);
}
void Rudders::set_trim(V3Attribute control_input){
        bool btrim =true;
        set_positions(control_input, btrim);
}
void Rudders::run(){
        left_rudder.deploy();
        right_rudder.deploy();
}
void Rudders::return_to_zero(){
        left_rudder.return_to_zero();
        right_rudder.return_to_zero();
}
void  Rudders::print(){
        left_rudder.print();
        right_rudder.print();
}
