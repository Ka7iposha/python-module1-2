class NonNegative:

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("значение должно быть больше 0")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Rectangle:
    width = NonNegative()
    height = NonNegative()

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return self._width * 2 + self._height * 2

    def square(self):
        return self._width * self._height

    def info(self):
        return self._width, self._height, self.perimeter(), self.square()


r = Rectangle(3, 4)

r.height = 0
print(r.height)

