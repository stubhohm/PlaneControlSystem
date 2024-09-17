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
        return self.get_value()
    
class BoolAtt(Attribute):
    def __init__(self, value:bool) -> None:
        super().__init__()
        self.set_value(value)

    def get_value(self) -> bool:
        if not self.value:
            self.set_value(False)
        return self.get_value()
    
class StrAtt(Attribute):
    def __init__(self, value:str) -> None:
        super().__init__()
        self.set_value(value)

    def get_value(self) -> str:
        if not self.value:
            self.set_value('No String Set')
        return self.get_value()

class Vect3Att(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.x = IntAtt(0)
        self.y = IntAtt(0)
        self.z = IntAtt(0)

    def get_normal(self):
        print('got normal')

class Vect2Att(Attribute):
    def __init__(self) -> None:
        super().__init__()
        self.x = IntAtt(0)
        self.y = IntAtt(0)
