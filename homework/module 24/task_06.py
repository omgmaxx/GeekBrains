class Fire:
    dscr = 'Первородная стихия - огонь'

    def __add__(self, other):
        if type(other) == Water:
            return Steam()
        elif type(other) == Air:
            return Lightning()
        elif type(other) == Earth:
            return Magma()
        else:
            return Slag()


class Water:
    dscr = 'Первородная стихия - вода'

    def __add__(self, other):
        if type(other) == Air:
            return Storm()
        elif type(other) == Earth:
            return Dirt()
        elif type(other) == Fire:
            return Steam()
        else:
            return Slag()


class Air:
    dscr = 'Первородная стихия - воздух'

    def __add__(self, other):
        if type(other) == Earth:
            return Dust()
        elif type(other) == Fire:
            return Lightning()
        elif type(other) == Water:
            return Storm()
        else:
            return Slag()


class Earth:
    dscr = 'Первородная стихия - земля'

    def __add__(self, other):
        if type(other) == Fire:
            return Magma()
        elif type(other) == Water:
            return Dirt()
        elif type(other) == Air:
            return Dust()
        else:
            return Slag()


class Storm:
    dscr = 'Сложный элемент - шторм'

    def __add__(self, other):
        return Slag()


class Steam:
    dscr = 'Сложный элемент - пар'

    def __add__(self, other):
        return Slag()


class Dirt:
    dscr = 'Сложный элемент - грязь'

    def __add__(self, other):
        return Slag()


class Lightning:
    dscr = 'Сложный элемент - молния'

    def __add__(self, other):
        return Slag()


class Dust:
    dscr = 'Сложный элемент - пыль'

    def __add__(self, other):
        return Slag()


class Magma:
    dscr = 'Сложный элемент - лава'

    def __add__(self, other):
        return Slag()


class Slag:
    dscr = 'Шлак, получившийся от неверного смешения'

    def __add__(self, other):
        return Slag()


fire = Fire()
water = Water()
air = Air()
earth = Earth()
storm = water + air
steam = fire + water
dirt = water + earth
light = air + fire
dust = air + earth
magma = fire + earth
slag = dust + storm


print(fire.dscr)
print(water.dscr)
print(air.dscr)
print(earth.dscr)
print(storm.dscr)
print(steam.dscr)
print(dirt.dscr)
print(light.dscr)
print(dust.dscr)
print(magma.dscr)
print(slag.dscr)
