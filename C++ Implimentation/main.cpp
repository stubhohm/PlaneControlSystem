#include "Modules\Setup\Setup.h"
#include "Modules\Loop\Loop.h"
#include "HelperFunctions\HelperFunctions.h"

int main(void){
    Plane black_bird = setup();
    loop(black_bird);
}
