"""
Generator Expressions
"""

def init_tuple():
    symbols = 'ABCDE'
    #  feeds the for one item at a time, saving memory
    #  the array is never built in memory, it's always one-by-one
    #  list comp actually builds that array
    a = tuple((ord(symbol) for symbol in symbols))
    print(a)


init_tuple()
