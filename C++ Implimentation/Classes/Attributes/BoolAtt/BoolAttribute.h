#ifndef BOOLATTRIBUTE_H
# define BOOLATTRIBUTE_H

class BoolAttribute {
private:
    bool value; //int attribute

public:
    // Constructor
    BoolAttribute(bool value);

    // Value Setter
    void setValue(bool newValue);

    // Value Getter
    bool getValue() const;

    // Value Inverter
    bool getNotValue() const;

    void print() const;
};

#endif