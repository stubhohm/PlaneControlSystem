import tracemalloc
tracemalloc.start()
from Classes.Plane import Plane
from Classes.InputClasses.Controller import Controller
from Classes.GeneralClasses.Attributes import Vect3Att

plane = Plane('SR 71')
controller = Controller()

def abort_loop(i:int):
    if i % 2 != 0:
        return True
    plane.print()
    plane.telemetry.print()
    response = input("Press 'Y' to abort: ").strip().lower()
    if 'y' in response:
        return False
    else:
        return True

def incriment_i(i:int):
    if i > 100:
        i = i % 100 
    else:
        i += 1
    print(i)
    return i

def init_variables():
    orient_pos = [0, 20, 0]
    trim_pos = [0 ,0, 0]
    orient = Vect3Att()
    orient.set(orient_pos)
    trim = Vect3Att()
    trim.set(trim_pos)
    return trim, orient

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