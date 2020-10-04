class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')
    def draw(self):
        print('draw')
    def print(self):
        print(f'x={self.x}, y={self.y}')

point1 = Point(10, 20)
print(point1.print())


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'My name is {self.name}')

person1 = Person('Ben')
person1.talk()
