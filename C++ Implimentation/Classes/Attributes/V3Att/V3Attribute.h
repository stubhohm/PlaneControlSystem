#ifndef V3ATTRIBUTE_H
#define V3ATTRIBUTE_H
#include "..\IntAtt\IntAttribute.h"
#include "..\Modules\Dependencies.h"

class V3Attribute {
private:
    IntAttribute x, y, z, minimum, maximum; //int attributes

int bind_vector(int value);

public:
    // Constructor
    V3Attribute(int x = 0, int y = 0, int z = 0);

// Component Setters
void setValue(int x, int y, int z);
void setValue(V3Attribute new_vector);
void setX(int newX);
void setY(int newY);
void setZ(int newZ);
void set_maximum(int new_max);
void set_minimum(int new_min);


// Component Getters
int getX() const;
int getY() const;
int getZ() const;
int get_minimum() const;
int get_maximum() const;

// Value Getter
V3Attribute getValue() const;

// Add method
V3Attribute add(V3Attribute vector);

// Subtract method
V3Attribute subtract(V3Attribute vector);

// Scale Vector method
V3Attribute scale_vector(int scaler);

int get_magnitude() const;

void print() const;
};

#endif