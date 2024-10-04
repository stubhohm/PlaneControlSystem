#include "Loop.h"

void loop(Plane black_bird){
    bool running = true;
    int i = 1;
    int throttle = 50;
    bool assist = false;
    bool gear_deploy = false;
    auto positional_vectors = init_variables();
    V3Attribute trim = positional_vectors.first;
    V3Attribute orient = positional_vectors.second;
    while (running){
        //controller.set(throttle, assist, gear_deploy, orient, trim);
        black_bird.impliment_control_inputs(assist, throttle, trim, orient);
        black_bird.run();
        black_bird.set_telemetry();

        running = abort_loop(i);
        i = incriment_i(i);
        }
}