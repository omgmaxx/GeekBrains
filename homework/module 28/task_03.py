from abc import ABC, abstractmethod
from math import sqrt


class Figures(ABC):
    def __init__(self, side: int) -> None:
        self._side = side

    @property
    def side(self) -> int:
        return self._side

    @side.setter
    def side(self, side: int) -> None:
        self._side = side

    @abstractmethod
    def square(self):
        pass


class Triangle(Figures):
    def __init__(self, side: int, base: int) -> None:
        super().__init__(side)
        self._base = base

    def __str__(self):
        return f'Треугольник со стороной {self._side} и основанием {self._base}'

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, base: int) -> None:
        self._base = base

    def square(self) -> float:
        return self._side * self._base / 2



class Square(Figures):
    def __init__(self, side: int) -> None:
        super().__init__(side)

    def __str__(self):
        return f'Квадрат со сторонами {self._side}'

    def square(self) -> int:
        return self._side ** 2


class VolumetricFigures(ABC):
    def __init__(self, figure_one):
        self.figures_list = []
        self._figure_one = figure_one

    @abstractmethod
    def volume(self):
        pass


class Cube(VolumetricFigures):
    def __init__(self, figure_one: Square):
        super().__init__(figure_one)
        for _ in range(6):
            self.figures_list.append(self._figure_one)

    def __str__(self):
        return 'Куб, состоящий из:\n'+'\n'.join([str(x) for x in self.figures_list])+'\n'

    @property
    def figure(self):
        return self._figure_one

    @property
    def volume(self):
        return self.figures_list[0].side ** 3


class Pyramid(VolumetricFigures):
    def __init__(self, figure_one: Triangle, figure_base: Square):
        super().__init__(figure_one)
        self._base = figure_base
        self._side = figure_one

        if figure_base.side == figure_one.base:
            for _ in range(4):
                self.figures_list.append(self._figure_one)
            self.figures_list.append(self._base)
        else:
            raise Exception('Стороны фигур не сходятся')

    def __str__(self):
        return 'Пирамида, состоящая из:\n'+'\n'.join([str(x) for x in self.figures_list])+'\n'

    @property
    def figure_side(self):
        return self._figure_one

    @property
    def figure_base(self):
        return self._base

    @property
    def volume(self):
        height = sqrt((sqrt(self._base.side ** 2 * 2) / 2) ** 2 + self._side.side ** 2)
        return self._base.side ** 2 * height / 3


square = Square(5)
cube = Cube(square)
triangle = Triangle(4, 5)
pyramid = Pyramid(triangle, square)
print(cube)
print(pyramid)
print(cube.volume)
print(pyramid.volume)
