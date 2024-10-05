#ifndef LOOP_H
#define LOOP_H

#include "..\..\Classes\Plane\Plane.h"
#include "..\HelperFunctions\HelperFunctions.h"

std::pair<V3Attribute, V3Attribute> init_variables();

void loop(Plane black_bird);

#endif