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
        if value <= 0:
            raise ValueError("ширина должна быть больше 0")
        self._width = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("высота должна быть больше 0")
        self._height = value


r = Rectangle(3, 4)
print(r.width)

r.width = -1
print(r.width)
