from math import pi, sqrt

class Circle:

    def __init__(self, x, y, radius):
        self.coords = {'x': x, 'y': y}
        self.radius = radius

    def s(self):
        square = pi * self.radius ** 2
        return round(square, 2)

    def p(self):
        perimeter = 2 * self.radius * pi
        return round(perimeter, 2)

    def multiply(self, k):
        self.radius *= k

    def check(self, another):
        if sqrt((another.coords['x'] - self.coords['x']) ** 2 + (another.coords['y'] - self.coords['y']) ** 2) \
                <= self.radius + another.radius:            # (x - x2)^2 + (y - y2)^2 <= r + r2
            print('Окружности пересекаются.\n')
        else:
            print('Окружности не пересекаются\n')

    def info(self):
        print('Координаты: X = {}, Y = {}\nРадиус: {}\n'.format(self.coords['x'], self.coords['y'], self.radius))


circ1 = Circle(5, 3, 3)
circ2 = Circle(11, 6, 1)

circ1.info()
circ2.info()

circ1.check(circ2)

circ2.multiply(4)

circ1.info()
circ2.info()

circ2.check(circ1)

print(f'\nПлощади окружностей: {circ1.s()}, {circ2.s()}\nПериметры окружностей: {circ1.p()}, {circ2.p()}')