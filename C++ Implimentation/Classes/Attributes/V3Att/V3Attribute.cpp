#include "V3Attribute.h"

// Constructor implimentation

V3Attribute::V3Attribute(int newX, int newY, int newZ)
    : x(newX), y(newY), z(newZ), minimum(-10000), maximum(10000)
    {
        setValue(newX, newY, newZ);
}

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

int V3Attribute::get_maximum() const{
    return maximum.getValue();
}

V3Attribute V3Attribute::getValue() const{
    int new_x = x.getValue();
    int new_y = y.getValue();
    int new_z = z.getValue();
    int new_max = maximum.getValue();
    int new_min = minimum.getValue();
    V3Attribute new_vector;
    new_vector.setValue(new_x, new_y, new_z);
    new_vector.set_maximum(new_max);
    new_vector.set_minimum(new_min);
    return new_vector;
}

int V3Attribute::get_minimum() const{
    return minimum.getValue();
}

int V3Attribute::bind_vector(int value){
    if (value < minimum.getValue()){
        value = abs(value);
        value = maximum.getValue() - value;
    } else if (value > maximum.getValue()){
        value = value % maximum.getValue();
    }
    return value;
}

void V3Attribute::setValue(int newX, int newY, int newZ){
    setX(newX);
    setY(newY);
    setZ(newZ);
}
void V3Attribute::setValue(V3Attribute new_vector){
    setX(new_vector.getX());
    setY(new_vector.getY());
    setZ(new_vector.getZ());
}

void V3Attribute::setX(int newX){
    newX = bind_vector(newX);
    x.setValue(newX);
}

void V3Attribute::setY(int newY){
    newY = bind_vector(newY);
    y.setValue(newY);
}
void V3Attribute::setZ(int newZ){
    newZ = bind_vector(newZ);
    z.setValue(newZ);
}

void V3Attribute::set_maximum(int new_max){
    maximum.setValue(new_max);
}

void V3Attribute::set_minimum(int new_min){
    minimum.setValue(new_min);
}

V3Attribute V3Attribute::add(V3Attribute vector){
    int sumx = vector.x.add(x.getValue());
    int sumy = vector.y.add(y.getValue());
    int sumz = vector.z.add(z.getValue());
    
    V3Attribute new_vector;
    new_vector.set_maximum(maximum.getValue());
    new_vector.set_minimum(minimum.getValue());
    new_vector.setValue(sumx, sumy, sumz);
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

void V3Attribute::print() const{
    std::cout << "Vector Readout x: "<< x.getValue() << " y: " << y.getValue() << " z: " << z.getValue()<< "\n";
}