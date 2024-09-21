#from Modules.Dependencies import sqrt

class Attribute():
    __slots__ = ['value']
    def __init__(self) -> None:
        self.value = None

    def get(self):
        return self.value
    
    def set(self, value):
        self.value = value

class IntAtt(Attribute):
    def __init__(self, value:int) -> None:
        super().__init__()
        self.set(value)

    def get(self) -> int:
        if not self.value:
            self.set(0)
        return super().get()
    
    def set(self, value:int):
        if type(value) not in [int, float]:
            return
        self.value = value
    
    def add(self, value:int):
        sum = self.get() + value
        return sum
    
    def subtract(self, value:int):
        difference = self.get() - value
        return difference
    
class BoolAtt(Attribute):
    def __init__(self, value:bool) -> None:
        super().__init__()
        self.set(value)

    def get(self) -> bool:
        if not self.value:
            self.set(False)
        return super().get()
    
    def set(self, value:bool):
        if type(value) != bool:
            return
        self.value = value

    def is_not(self):
        return not self.get()
    
class StrAtt(Attribute):
    __slots__ = ['value']
    def __init__(self, value:str) -> None:
        super().__init__()
        self.set(value)

    def get(self) -> str:
        if not self.value:
            self.set('No String Set')
        return super().get()
    
    def set(self, value:str):
        if type(value) != str:
            return
        self.value = value

    def lower(self):
        return self.get().lower()
    
    def upper(self):
        return self.get().upper()
    
    def capitalize(self):
        return self.get().capitalize()

class Vect3Att(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.x = IntAtt(0)
        self.y = IntAtt(0)
        self.z = IntAtt(0)
        self.set(self)
        self.maximum = IntAtt(0)
        self.minimum = IntAtt(0)

    def get_normal(self):
        print('got normal')

    def __set_from_tuple(self, vector:tuple[int|float,int|float,int|float]):
        self.x.set(vector[0])
        self.y.set(vector[1])
        self.z.set(vector[2])
        self.value = vector

    def __to_tuple(self, vector: 'Vect3Att'):
            vector_tuple = (vector.x.get(), vector.y.get(), vector.z.get())
            return vector_tuple

    def set(self, value: 'Vect3Att'):
        if type(value) == Vect3Att:
            value = self.__to_tuple(value)
        self.__set_from_tuple(value)
        

    def get(self) -> tuple[int,int,int]:
        vector_tuple = super().get()
        if type(vector_tuple) != tuple:
            vector_tuple = [0, 0, 0]
        return vector_tuple

    def scale_vector(self, scaler:float):
        x = self.x.get() * scaler
        y = self.y.get() * scaler
        z = self.z.get() * scaler
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
        magnitude = sqrt(summation)
        return magnitude
        
class Vect2Att(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.x = IntAtt(0)
        self.y = IntAtt(0)
        self.set(self)

    def __set_from_tuple(self, vector:tuple[int|float, int|float]):
        self.x.set(vector[0])
        self.y.set(vector[1])
        self.value = vector

    def __to_tuple(self, vector: 'Vect2Att'):
            vector_tuple = (vector.x.get(), vector.y.get())
            return vector_tuple

    def set(self, value: 'Vect2Att'):
        if type(value) == Vect2Att:
            value = self.__to_tuple(value)
        self.__set_from_tuple(value)

    def get(self) -> tuple[int,int]:
        vector_tuple = super().get()
        if type(vector_tuple) != tuple:
            vector_tuple = [0, 0]
        return vector_tuple    

    def scale_vector(self, scaler:float):
        x = self.x.get() * scaler
        y = self.y.get() * scaler
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
        magnitude = sqrt(summation)
        return magnitude

