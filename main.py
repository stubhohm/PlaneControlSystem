import tracemalloc
tracemalloc.start()

from SetupFunctions.Functions import abort_loop, incriment_i, init_variables, plane, controller

def setup():
    throttle = 5
    plane.startup_sequence()
    plane.engines.set_thrust(throttle)
    while not plane.landing_gear.is_deployed():
        plane.run()
        plane.landing_gear.print()

def loop():
    running = True
    i = 1
    throttle = 50
    assist = False
    gear_deploy = False
    trim, orient = init_variables()
    while running:
        controller.set(throttle, assist, gear_deploy, orient, trim)
        plane.impliment_control_inputs(assist, throttle, trim, orient)
        plane.run()
        plane.set_telemetry()

        running = abort_loop(i)
        i = incriment_i(i)

setup()
loop()

# Get the current memory usage
current, peak = tracemalloc.get_traced_memory()

print(f"Current memory usage: {current / 1024} KB")
print(f"Peak memory usage: {peak / 1024} KB")

# Stop tracking memory
tracemalloc.stop()