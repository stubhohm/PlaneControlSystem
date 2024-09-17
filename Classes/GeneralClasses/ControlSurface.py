from .Attributes import IntAtt, StrAtt

class ControlSurface():
    def __init__(self) -> None:
        self._starting_position = IntAtt(0)
        self._current_position = IntAtt(0)
        self._starting_position = IntAtt(0)
        self.target_position = IntAtt(0)
        self._max_position = IntAtt(100)
        self._min_position = IntAtt(-100)
        self._trim = IntAtt(0)
        self.target_trim = IntAtt(0)
        self.change_rate = IntAtt(5)
        self.target_tolerance = IntAtt(int(self.change_rate.get_value()/2 + 1))
        self.name = StrAtt()

    def __bind_target_position(self):
        if self.target_position.get_value() > self._max_position.get_value():
            self.target_position.set_value(self._max_position.get_value())
        if self.target_position.get_value() < self._min_position.get_value():
            self.target_position.set_value(self._min_position.get_value())
        
    def __bind_trim(self):
        if self.target_trim.get_value() > self._max_position.get_value():
            self.target_trim.set_value(self._max_position.get_value())
        if self.target_trim.get_value() < self._min_position.get_value():
            self.target_trim.set_value(self._min_position.get_value())

    def __is_in_tolerance(self, include_trim = False):
        distance_to_target = self._current_position.get_value() - self.target_position.get_value()
        if include_trim:
            distance_to_target += self._trim.get_value()
        in_tolerance = (abs(distance_to_target) < self.target_tolerance.get_value())
        return in_tolerance

    def __incriment_position(self):
        change = self.change_rate.get_value()
        if self._current_position.get_value() > self.target_position.get_value():
            change *= -1
        self._current_position.set_value(self._current_position.get_value() + change)

    def __incriment_trim(self):
        change = int(self.change_rate.get_value() / 2)
        if self._trim.get_value() > self.target_trim.get():
            change *= -1
        self._trim.set_value(self._trim.get_value() + change)

    def return_to_zero(self):
        if self.__is_in_tolerance(True):
            return
        self.target_position.set_value(self._trim.get_value() + 0)
        self.__incriment_position()
        self.__incriment_trim()

    def move_to_target(self):
        if self.__is_in_tolerance(True):
            return
        self.__incriment_position()
        self.__incriment_trim()

    def set_target_position(self, value:int):
        self.target_position.set_value(value)
        self.__bind_target_position()

    def set_target_trim(self, value:int):
        self.target_trim.set_value(value)
        self.__bind_trim()