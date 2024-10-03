#include "BoolAttribute.h"
#include "Wheel\Wheel.h"


class LandingGear{
private: 
    Wheel left, right, front;
    BoolAttribute moving, deployed, retracted, stow_great;

void print_wheel_states(self){
        front.print_wheel_bools('Front');
        left.print_wheel_bools('Left');
        right.print_wheel_bools('Right');
}

void deploy(self){
        bool a,b,c,d,e,f;

        a, d = self.__left.deploy();
        b, e = self.__right.deploy();
        c, f = self.__front.deploy();
        
        if (true in [a, b, c]){
            self.__moving.set(true);
            self.__retracted.set(false);
            self.__deployed.set(false);
        } elif (false not in [d, e, f]){
            self.__deployed.set(true);
            self.__moving.set(false);
            }
}

public:

void deploy_gear(){
        stow_gear.setValue(false);
}
void retract_gear(){
        stow_gear.setValue(true);
}

BoolAttribute is_deployed(){
        return deployed;
}

BoolAttribute is_stowed(self):
        return retracted;

void run(){
        if (stow_gear.getValue()){
            retract();
            } else {
            deploy();
            }
}

            

    
    def __retract(self):
        a, d = self.__left.retract()
        b, e = self.__right.retract()
        c, f = self.__front.retract()
        if True in [a, b, c]:
            self.__moving.set(True)
            self.__retracted.set(False)
            self.__deployed.set(False)
        elif True not in [d, e, f]:
            self.__retracted.set(True)
            self.__moving.set(False)

    def engage_brakes(self):
        self.__front.engage_brakes()
        self.__left.engage_brakes()
        self.__right.engage_brakes()

    def release_brakes(self):
        self.__front.release_brakes()
        self.__left.release_brakes()
        self.__right.release_brakes()

    def print(self):
        print(f'\nMoving: {self.__moving.get()} \nDeployed: {self.__deployed.get()} \nRetracted: {self.__retracted.get()}')
        self.__print_wheel_states()