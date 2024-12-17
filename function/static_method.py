# This is an example of a static method in Python
# Static methods are methods that belong to the class itself, not to any particular object.
# They are defined with the @staticmethod decorator.
# They are used when a method does not need to access any instance-specific data (self or cls).
# In this example, the add and substract methods are static methods.
# They do not need to access any instance-specific data, so they are defined as static methods.
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def substract(x,y):
        return x - y
