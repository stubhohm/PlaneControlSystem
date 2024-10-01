from Classes.GeneralClasses.Attributes import Vect3Att
from Classes.Plane import Plane
from Classes.InputClasses.Controller import Controller

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