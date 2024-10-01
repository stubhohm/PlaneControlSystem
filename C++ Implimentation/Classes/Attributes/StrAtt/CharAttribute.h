#ifndef CHARATTRIBUTE_H
# define CHARATTRIBUTE_H

class CharAttribute {
private:
    char value; //int attribute

public:
    // Constructor
    CharAttribute(char value);

    // Value Setter
    void setValue(char newValue);

    // Value Getter
    char getValue() const;

};

#endif