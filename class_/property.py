class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width*self._height
    
def main():
    rec = Rectangle(3, 5)
    print(rec.area)
