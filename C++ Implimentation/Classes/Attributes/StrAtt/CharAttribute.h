#ifndef CHARATTRIBUTE_H
# define CHARATTRIBUTE_H
#include "..\..\..\Modules\Dependencies.h"

class CharAttribute {
private:
    std::string value; //int attribute

public:
    // Constructor
    CharAttribute(std::string value = "Unnamed");

    // Value Setter
    void setValue(std::string newValue);

    // Value Getter
    std::string getValue() const;

    void print() const;

};

#endif