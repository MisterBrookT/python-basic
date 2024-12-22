from abc import ABC, abstractmethod

# define abstract class
# abc stands for Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def sound(self):
        pass
    
    @staticmethod
    def say_hello():
        print("Hello!")


class Cat(Animal):
    def move(self):
        print("Cat moves")

    def sound(self):
        print("Cat meows")

cat = Cat()
cat.move()
cat.sound()
cat.say_hello()
