#include "BoolAttribute.h"

// Constructor implimentation

BoolAttribute::BoolAttribute(bool value = false)
    : value(value) {}

// Getter for value
bool BoolAttribute::getValue() const{
    return value;
}

// Setter for value
void BoolAttribute::setValue(bool newValue){
    value = newValue;
}

bool BoolAttribute::getNotValue() const{
    if(value == true){
        return false;
    } else {
        return true;
    }
}

void BoolAttribute::print() const{
    std::cout << "Int Value: " << value << "\n";
}