from Classes.Plane import Plane
from Classes.InputClasses import Controller

plane = Plane('SR 71')
controller = Controller()

def abort_loop(i:int):
    if i % 10 != 0:
        return
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


def main():
    running = True
    i = 1
    while running:
        running = abort_loop(i)
        i = incriment_i(i)


        


main()