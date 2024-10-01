#ifndef INTATTRIBUTE_H
# define INTATTRIBUTE_H

class IntAttribute {
private:
    int value; //int attribute

public:
    // Constructor
    IntAttribute(int value);

    // Value Setter
    void setValue(int newValue);

    // Value Getter
    int getValue() const;

    // Add method
    int add(int amount);

    // Subtract method
    int subtract(int amount);
};

#endif