"""
Code example from Fluent in Python
"""

from math import hypot

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    #  get the string representation of the object
    #  used in %r
    #  Also notice this will return a string that matches the constructor syntax
    #  favoring this over __str__
    #  https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
    def __repr__(self):
        return 'Vector(%r, %r)'%(self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    #  Notice that even in this dunder method, the author didn't call "self.__abs__"
    #  still using abs(), the built-in function
    #  if not implemented, __len__ will be called, 0 --> False, otherwise --> True
    def __bool__(self):
        return bool(abs(self))

    """
    Arithmetic operators
        1.) a new instance is returned
        2.) self other scalar not modified
    I think this is similar to C++ operator overloading?
    Q: What happens if other is not of type Vector?
    A: seems it can still work sometimes. see experiments in main()
    """

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
        

def main():
    v = Vector(3,4)

    print(v)

    print("Vector is %r"%v)

    print("Vector is %s"%v)

    u = Vector(4,3)
    print("Vector v %r adds Vector u %r gives Vector x %r"%(v, u, v+u))

    #  u + a will give an error
    #a = (3,2)
    #print("Vector v %r adds tuple a %r gives x %r"%(v, a, v+a))

    #  So apparently, this will work, despite the fact that not_vector is not actually Vector
    import collections
    not_vector = collections.namedtuple('Not_vector', ['x', 'y'])
    a = not_vector(3,4)
    print("Vector v %r adds not_vector a %r gives x %r"%(v, a, v+a))



if __name__ == "__main__":
    main()
