#include "CharAttribute.h"

// Constructor implimentation

CharAttribute::CharAttribute(char* value)
    : value(value) {}

// Getter for value
char* CharAttribute::getValue() const{
    return value;
}

// Setter for value
void CharAttribute::setValue(char* newValue){
    value = newValue;
}

void CharAttribute::print() const{
    std::cout << "string: " << &value << "\n";
}
