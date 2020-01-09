"""
List compression
"""
def demo1():
    x = 'my precious'
    #  notice here, this list comp has its own scope
    #  so the first two "x" will be interpreted as the iterable
    #  but the last x is still the string defined above
    list = [x for x in x]
    print(list)

    #  another example
    y = 'ABC'
    dummy = [ord(y) for y in y]
    print(dummy)
    print(y)

def cartesian_product():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)
    
    #  spaces are ignored inside pairs of [], {}, and ()
    tshirts = [(color, size) for color in colors
                             for size in sizes]
    print(tshirts)

    #  does zip work? NO, because zip enforces the same index
    #  cartesian product requires each element in this list to multiply with every other element in the other list
    tshirts = [x for x in zip(colors, sizes)]
    print(tshirts)


cartesian_product()
#demo1()

