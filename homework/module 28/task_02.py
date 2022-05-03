import math
from typing import Union


class MyMath:
    @classmethod
    def circle_len(cls, radius: Union[int, float]) -> float:
        return math.pi * radius * 2

    @classmethod
    def circle_sq(cls, radius: Union[int, float]) -> float:
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, c_edge: Union[int, float]) -> Union[int, float]:
        return c_edge ** 3

    @classmethod
    def sphere_surface(cls, radius: Union[int, float]) -> float:
        return math.pi * 4 * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(c_edge=5)
res_4 = MyMath.sphere_surface(radius=4)
print(res_1)
print(res_2)
print(res_3)
print(res_4)
