#include "CharAttribute.h"

// Constructor implimentation

CharAttribute::CharAttribute(std::string value)
    : value(value) {}

// Getter for value
std::string CharAttribute::getValue() const{
    return value;
}

// Setter for value
void CharAttribute::setValue(std::string newValue){
    value = newValue;
}

void CharAttribute::print() const{
    std::cout << "string: " << &value << "\n";
}
