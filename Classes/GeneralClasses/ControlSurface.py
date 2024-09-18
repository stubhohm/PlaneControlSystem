from .Attributes import IntAtt, StrAtt

class ControlSurface():
    def __init__(self) -> None:
        self.__starting_position = IntAtt(0)
        self.current_position = IntAtt(0)
        self.__starting_position = IntAtt(0)
        self.target_position = IntAtt(0)
        self.max_position = IntAtt(100)
        self.min_position = IntAtt(-100)
        self.__trim = IntAtt(0)
        self.target_trim = IntAtt(0)
        self.change_rate = IntAtt(5)
        self.target_tolerance = IntAtt(int(self.change_rate.get_value()/2 + 1))
        self.name = StrAtt('Unnamed Control Surface')

    def __bind_target_position(self):
        if self.target_position.get_value() > self.max_position.get_value():
            self.target_position.set_value(self.max_position.get_value())
        if self.target_position.get_value() < self.min_position.get_value():
            self.target_position.set_value(self.min_position.get_value())
        
    def __bind_trim(self):
        if self.target_trim.get_value() > self.max_position.get_value():
            self.target_trim.set_value(self.max_position.get_value())
        if self.target_trim.get_value() < self.min_position.get_value():
            self.target_trim.set_value(self.min_position.get_value())

    def __is_in_tolerance(self, include_trim = False):
        distance_to_target = self.current_position.get_value() - self.target_position.get_value()
        if include_trim:
            distance_to_target += self.__trim.get_value()
        in_tolerance = (abs(distance_to_target) < self.target_tolerance.get_value())
        return in_tolerance

    def __incriment_position(self):
        change = self.change_rate.get_value()
        if self.current_position.get_value() > self.target_position.get_value():
            change *= -1
        self.current_position.set_value(self.current_position.get_value() + change)

    def __incriment_trim(self):
        change = int(self.change_rate.get_value() / 2)
        if self.__trim.get_value() > self.target_trim.get_value():
            change *= -1
        self.__trim.set_value(self.__trim.get_value() + change)

    def return_to_zero(self):
        if self.__is_in_tolerance(True):
            return
        self.target_position.set_value(self.__trim.get_value() + 0)
        self.__incriment_position()
        self.__incriment_trim()

    def move_to_target(self):
        if self.__is_in_tolerance(True):
            return True
        self.__incriment_position()
        self.__incriment_trim()
        return False

    def set_target_position(self, value:int):
        '''Sets the target position within the bounds set by the max and min of the control component.'''
        self.target_position.set_value(value)
        self.__bind_target_position()

    def set_target_trim(self, value:int):
        '''Sets the targt trim valout within the bounds to the trim binding which is based on the total min and max ranges.'''
        self.target_trim.set_value(value)
        self.__bind_trim()