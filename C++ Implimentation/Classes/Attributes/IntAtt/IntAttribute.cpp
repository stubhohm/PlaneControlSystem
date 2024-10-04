#include "IntAttribute.h"

// Constructor implimentation

IntAttribute::IntAttribute(int value)
    : value(value) {}

// Getter for value

int IntAttribute::getValue() const{
    return value;
}

void IntAttribute::setValue(int newValue){
    value = newValue;
}

int IntAttribute::add(int amount){
    int summation = value + amount;
    return summation;
}

int IntAttribute::subtract(int amount){
    int difference = value - amount;
    return difference;
}

void IntAttribute::print() const{
    std::cout << "Int Value: " << value << "\n";
}