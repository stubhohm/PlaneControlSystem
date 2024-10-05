#ifndef BAROMETER_H
# define BAROMETER_H
#include "..\..\Attributes\IntAtt\IntAttribute.h"

class Barometer {
private:
    IntAttribute delta_p;

public:

    Barometer();

void setValue(int value);

int getValue();
};

#endif