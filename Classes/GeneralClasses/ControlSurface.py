from .Attributes import IntAtt, StrAtt
slots = ['__starting_position', 'current_position', 'target_position',
         'max_position', 'min_position', '__trim', 'target_trim', 'change_rate',
         'target_tolerance', 'name']
class ControlSurface():
    __slots__ = slots
    def __init__(self) -> None:
        self.__starting_position = IntAtt(0)
        self.current_position = IntAtt(0)
        self.target_position = IntAtt(0)
        self.max_position = IntAtt(100)
        self.min_position = IntAtt(-100)
        self.__trim = IntAtt(0)
        self.target_trim = IntAtt(0)
        self.change_rate = IntAtt(5)
        self.target_tolerance = IntAtt(int(self.change_rate.get()/2 + 1))
<<<<<<< HEAD
        self.name = StrAtt('Unnamed')
=======
        self.name = StrAtt('Unnamed Control Surface')
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153

    def __bind_target_position(self):
        if self.target_position.get() > self.max_position.get():
            self.target_position.set(self.max_position.get())
        if self.target_position.get() < self.min_position.get():
            self.target_position.set(self.min_position.get())
        
    def __bind_trim(self):
        if self.target_trim.get() > self.max_position.get():
            self.target_trim.set(self.max_position.get())
        if self.target_trim.get() < self.min_position.get():
            self.target_trim.set(self.min_position.get())

    def __is_in_tolerance(self, include_trim = False):
        distance_to_target = self.current_position.get() - self.target_position.get()
        if include_trim:
            distance_to_target += self.__trim.get()
        in_tolerance = (abs(distance_to_target) < self.target_tolerance.get())
        return in_tolerance

    def __incriment_position(self):
        change = self.change_rate.get()
        if self.current_position.get() > self.target_position.get():
            change *= -1
        self.current_position.set(self.current_position.get() + change)

    def __incriment_trim(self):
        change = int(self.change_rate.get() / 2)
        if self.__trim.get() > self.target_trim.get():
            change *= -1
        self.__trim.set(self.__trim.get() + change)

    def return_to_zero(self):
        self.target_position.set(self.__trim.get() + 0)
        if self.__is_in_tolerance(True):
<<<<<<< HEAD
            return
        self.target_position.set(self.__trim.get() + 0)
        self.__incriment_position()
        self.__incriment_trim()
=======
            return True
        print(self.target_position.get())
        return self.move_to_target()
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153

    def move_to_target(self):
        if self.__is_in_tolerance(True):
            return True
        self.__incriment_position()
        self.__incriment_trim()
        return False

    def set_target_position(self, value:int|float):
        '''Sets the target position within the bounds set by the max and min of the control component.'''
<<<<<<< HEAD
=======
        value = int(value)
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153
        self.target_position.set(value)
        self.__bind_target_position()

    def set_target_trim(self, value:int|float):
        '''Sets the targt trim valout within the bounds to the trim binding which is based on the total min and max ranges.'''
<<<<<<< HEAD
=======
        value = int(value)
>>>>>>> 85956aa976b3cb76df5bbafe2e36c0b1b148c153
        self.target_trim.set(value)
        self.__bind_trim()