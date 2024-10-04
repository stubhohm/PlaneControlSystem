#ifndef CHARATTRIBUTE_H
# define CHARATTRIBUTE_H
#include "..\Modules\Dependencies.h"

class CharAttribute {
private:
    char* value; //int attribute

public:
    // Constructor
    CharAttribute(char* value);

    // Value Setter
    void setValue(char* newValue);

    // Value Getter
    char* getValue() const;

    void print() const;

};

#endif