import functools


def singleton(cls):
    @functools.wraps(cls)
    def wrapping(*args, **kwargs):
        if not wrapping.instance:
            wrapping.instance = cls(*args, **kwargs)
        return wrapping.instance
    wrapping.instance = None
    return wrapping

@singleton
class Example:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)


obj1 = Example(15)
obj2 = Example(25)

print(id(obj1))
print(id(obj2))

print(obj1)
print(obj2)
