#include "V3Attribute.h"
#include <math.h>

// Constructor implimentation

V3Attribute::V3Attribute(int x, int y, int z)
    : setX(x), setY(y), setZ(z) {}

// Getter for values
int V3Attribute::getX() const{
    return x.getValue();
}
int V3Attribute::getY() const{
    return y.getValue();
}
int V3Attribute::getZ() const{
    return z.getValue();
}

void V3Attribute::setX(int newX){
    x.setValue(newX);
}
void V3Attribute::setY(int newY){
    y.setValue(newY);
}
void V3Attribute::setZ(int newZ){
    z.setValue(newZ);
}

V3Attribute V3Attribute::add(V3Attribute vector){
    int sumx = vector.x.add(x.getValue());
    int sumy = vector.y.add(y.getValue());
    int sumz = vector.z.add(z.getValue());
    V3Attribute new_vector(sumx, sumy, sumz);
    return new_vector;
}

V3Attribute V3Attribute::subtract(V3Attribute vector){
    int sumx = vector.x.subtract(x.getValue());
    int sumy = vector.y.subtract(y.getValue());
    int sumz = vector.z.subtract(z.getValue());
    V3Attribute new_vector(sumx, sumy, sumz);
    return new_vector;
}

int V3Attribute::get_magnitude() const{
    int summation = (getX() * getX()) + (getY() * getY()) + (getZ() * getZ());
    double magnitude = sqrt(summation);
    int int_magnitude = (int)magnitude;
    return int_magnitude;
}

V3Attribute V3Attribute::scale_vector(int scaler){
    int newX = getX() * scaler;
    int newY = getY() * scaler;
    int newZ = getZ() * scaler;
    V3Attribute new_vector(newX, newY, newZ);
    return new_vector;
}