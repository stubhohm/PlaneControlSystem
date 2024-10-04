#ifndef V3ATTRIBUTE_H
#define V3ATTRIBUTE_H
#include "..\IntAtt\IntAttribute.h"
#include "..\Modules\Dependencies.h"

class V3Attribute {
private:
    IntAttribute x, y, z; //int attributes

public:
    // Constructor
    V3Attribute(int x = 0, int y = 0, int z = 0);

    // Component Setters
    void set_value(int x, int y, int z);
    void setX(int newX);
    void setY(int newY);
    void setZ(int newZ);

    // Component Getters
    int getX() const;
    int getY() const;
    int getZ() const;

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