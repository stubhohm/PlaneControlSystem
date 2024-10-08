#include "ControlSurface.h"


ControlSurface::ControlSurface()
      : starting_position(0),
        current_position(0),
        target_position(0),
        max_position(100),
        min_position(-100),
        trim(0),
        target_trim(0),
        change_rate(5),
        target_tolerance((change_rate.getValue() >> 1) + 1),
        name("u")
{}

void ControlSurface::bind_target_position(){
    int max_value = max_position.getValue();
    int min_value = min_position.getValue();
    int tgt_pos = target_position.getValue();
    if (tgt_pos > max_value){
        target_position.setValue(max_value);
    } else if (tgt_pos < min_value){
        target_position.setValue(min_value);
    }
}

void ControlSurface::bind_trim(){
    int tgt_trim = target_trim.getValue();
    int max_trim = max_position.getValue();
    int min_trim = min_position.getValue();
    
    if (tgt_trim > max_trim) {
        target_trim.setValue(max_trim);
    } else if (tgt_trim < min_trim) {
        target_trim.setValue(min_trim);
    }
}

BoolAttribute ControlSurface::is_in_tolerance(bool include_trim){
    int distance_to_target = current_position.getValue() - target_position.getValue();
    if (include_trim) {
        distance_to_target += trim.getValue();
    }
    BoolAttribute in_tolerance(abs(distance_to_target) < target_tolerance.getValue());
    return in_tolerance;
}

void ControlSurface::incriment_position(){
    int change = change_rate.getValue();
    if (current_position.getValue() > target_position.getValue()){
        change *= -1;
    }
    int new_position = current_position.getValue() + change;
    current_position.setValue(new_position);
}

void ControlSurface::incriment_trim(){
        int change = change_rate.getValue() >> 1;
        if (trim.getValue() > target_trim.getValue()){
            change *= -1;
        } else {
        trim.setValue(trim.getValue() + change);
        }
}

BoolAttribute ControlSurface::return_to_zero(){
    target_position.setValue(trim.getValue() + 0);
    BoolAttribute bool_value(true);
    if (is_in_tolerance(true).getValue()) {
        return bool_value;
    } else {
    bool_value = move_to_target();
    return bool_value;
    }
}

BoolAttribute ControlSurface::move_to_target(){
    BoolAttribute bool_value = true;
    if (is_in_tolerance(true).getValue()){
        return bool_value;
    } else {
    incriment_position();
    incriment_trim();
    bool_value.setValue(false);
    return bool_value;
    }
}

void ControlSurface::set_target_position(int target_value){
    target_position.setValue(target_value);
    bind_target_position();
}

void ControlSurface::set_target_trim(int target_value){
    target_trim.setValue(target_value);
    bind_trim();
}