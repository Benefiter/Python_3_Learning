class Pet:
    def walk(self):
        print('walk')


class Dog(Pet):
    def bark(self):
        print('bark')

class Cat(Pet):
    pass


cat = Cat()
print(cat.walk())
dog = Dog()
print(dog.walk())
dog.bark()