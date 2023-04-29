class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return self._width*2 + self._height*2

    def square(self):
        return self._width * self._height

    def info(self):
        return self._width, self._height, self.perimeter(), self.square()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


r = Rectangle(3, 4)
print(r.height)

r.height = 5
print(r.height)