#include "Engine.h"

void Engine::name_components(){
    if (laterality == left){
        std::string side = "L";
    } else {
        std::string side = "R";
    }
    air_spike.name.setValue("{side} Air Spike");
    throttle.name.setValue("{side} Throttle");
    nozzle.name.setValue("{side} Nozzle");
}

    
    Engine::Engine(bool laterality){
    laterality = laterality;
    is_active.setValue(false);
    name_components();
}


void Engine::run(){
    if (get_engine_state().getValue()){
    throttle.run();
    air_spike.run();
    nozzle.run();
    }
}

void Engine::activate_engine(){
    is_active.setValue(true);
}

void Engine::deactivate_engine(){
    is_active.setValue(false);
}

BoolAttribute Engine::get_engine_state(){
    return is_active;
}

int Engine::get_throttle(){
    return throttle.get_current_position();
}

void Engine::set_throttle(int new_throttle){
    throttle.set_target_position(new_throttle);
}

void Engine::print(std::string){
    int current_throttle = get_throttle();
    int tgt_throttle = throttle.target_position.getValue();
    bool active = get_engine_state().getValue();
    int air_spike_pos = air_spike.current_position.getValue();
    int nozzle_pos = nozzle.current_position.getValue();
    /* print()
    print(f'{position} Eng: {active}')
    print(f'Tht:{throttle}')
    print(f'Tgt Tht:{tgt_throttle}')
    print(f'Aspk Pos {air_spike}')
    print(f'Nzl Pos {nozzle}') */
}
