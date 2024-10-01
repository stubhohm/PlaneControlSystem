#ifndef V3ATTRIBUTE_H
#define V3ATTRIBUTE_H
#include "IntAttribute.h"

class V3Attribute {
private:
    IntAttribute x; //int attribute
    IntAttribute y; //int attribute
    IntAttribute z; //int attribute

public:
    // Constructor
    V3Attribute(int x, int y, int z);

    // Component Setters
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
    void scale_vector(int scaler);

    int get_magnitude() const;
};

#endif