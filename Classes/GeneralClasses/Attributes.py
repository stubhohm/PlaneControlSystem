from Modules.Dependencies import math

class Attribute():
    def __init__(self) -> None:
        self.value = None

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

class IntAtt(Attribute):
    def __init__(self, value:int) -> None:
        super().__init__()
        self.set_value(value)

    def get_value(self) -> int:
        if not self.value:
            self.set_value(0)
        return super().get_value()
    
    def set_value(self, value:int):
        self.value = value
    
    def add(self, value:int):
        sum = self.get_value() + value
        return sum
    
    def subtract(self, value:int):
        difference = self.get_value() - value
        return difference
    
class BoolAtt(Attribute):
    def __init__(self, value:bool) -> None:
        super().__init__()
        self.set_value(value)

    def get_value(self) -> bool:
        if not self.value:
            self.set_value(False)
        return super().get_value()
    
    def set_value(self, value:bool):
        self.value = value
    
class StrAtt(Attribute):
    def __init__(self, value:str) -> None:
        super().__init__()
        self.set_value(value)

    def get_value(self) -> str:
        if not self.value:
            self.set_value('No String Set')
        return super().get_value()
    
    def set_value(self, value:str):
        self.value = value

class Vect3Att(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.x = IntAtt(0)
        self.y = IntAtt(0)
        self.z = IntAtt(0)
        self.set_value(self)
        self.maximum = IntAtt(0)
        self.minimum = IntAtt(0)

    def get_normal(self):
        print('got normal')

    def __set_value_from_tuple(self, vector:tuple[int,int,int]):
        self.x.set_value(vector[0])
        self.y.set_value(vector[1])
        self.z.set_value(vector[2])
        self.value = vector

    def __to_tuple(self, vector: 'Vect3Att'):
            vector_tuple = (vector.x.get_value(), vector.y.get_value(), vector.z.get_value())
            return vector_tuple

    def set_value(self, value: 'Vect3Att'):
        if type(value) == Vect3Att:
            value = self.__to_tuple(value)
        self.__set_value_from_tuple(value)
        

    def get_value(self) -> tuple[int,int,int]:
        vector_tuple = super().get_value()
        if type(vector_tuple) != tuple:
            vector_tuple = [0, 0, 0]
        return vector_tuple

    def scale_vector(self, scaler:float):
        x = self.x.get_value() * scaler
        y = self.y.get_value() * scaler
        z = self.z.get_value() * scaler
        return (x, y, z)
    
    def add_vector(self, vector: 'Vect3Att'):
        vector_1 = self.__to_tuple(self)
        if type(vector) == Vect3Att:
            vector = self.__to_tuple(vector)
        x = vector[0] + vector_1[0]
        y = vector[1] + vector_1[1]
        z = vector[2] + vector_1[2]
        return (x, y, z)
    
    def get_magnitude(self):
        tuple = self.__to_tuple(self)
        summation = 0
        for i in range(len(tuple)):
            summation += (tuple[i] * tuple[i])
        magnitude = math.sqrt(summation)
        return magnitude
        
class Vect2Att(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.x = IntAtt(0)
        self.y = IntAtt(0)
        self.set_value(self)

    def __set_value_from_tuple(self, vector:tuple[int,int]):
        self.x.set_value(vector[0])
        self.y.set_value(vector[1])
        self.value = vector

    def __to_tuple(self, vector: 'Vect2Att'):
            vector_tuple = (vector.x.get_value(), vector.y.get_value())
            return vector_tuple

    def set_value(self, value: 'Vect2Att'):
        if type(value) == Vect2Att:
            value = self.__to_tuple(value)
        self.__set_value_from_tuple(value)

    def get_value(self) -> tuple[int,int]:
        vector_tuple = super().get_value()
        if type(vector_tuple) != tuple:
            vector_tuple = [0, 0]
        return vector_tuple    

    def scale_vector(self, scaler:float):
        x = self.x.get_value() * scaler
        y = self.y.get_value() * scaler
        return (x, y)
    
    def add_vector(self, vector: 'Vect2Att'):
        vector_1 = self.__to_tuple(self)
        if type(vector) == Vect2Att:
            vector = self.__to_tuple(vector)
        x = vector[0] + vector_1[0]
        y = vector[1] + vector_1[1]
        return (x, y)
    
    def get_magnitude(self):
        tuple = self.__to_tuple(self)
        summation = 0
        for i in range(len(tuple)):
            summation += (tuple[i] * tuple[i])
        magnitude = math.sqrt(summation)
        return magnitude
