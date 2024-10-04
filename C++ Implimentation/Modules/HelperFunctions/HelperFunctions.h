#ifndef HELPERFUNCTIONS_H
#define HELPERFUNCTIONS_H

#include "..\V3Att\V3Attribute.h"

std::pair<V3Attribute, V3Attribute> init_variables();

bool abort_loop(int i);

int incriment_i(int i);

float cosine_lookup(int angle);

float sine_lookup(int angle);

float sqrt(float n);

float sqrt(int n);

float abs(float value);

int abs(int value);

#endif