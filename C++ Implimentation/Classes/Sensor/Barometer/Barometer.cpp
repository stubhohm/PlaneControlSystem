#include "Barometer.h"

    Barometer::Barometer()
    : delta_p(0){}

void Barometer::setValue(int value){
    delta_p.setValue(value);
}

int Barometer::getValue(){
    return delta_p.getValue();
}