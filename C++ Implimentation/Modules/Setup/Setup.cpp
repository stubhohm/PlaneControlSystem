#include "Setup.h"

Plane setup(){
    Plane black_bird("SR-71 Blackbird");
    int throttle = 5;
    black_bird.startup_sequence();
    black_bird.engines.set_thrust(throttle);
    while (black_bird.landing_gear.is_deployed().getNotValue())
        black_bird.run();
        black_bird.landing_gear.print();
    return black_bird;
}