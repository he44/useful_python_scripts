def tuple_as_record():
    traveler_ids = [
        (120, "USA", "1111111"),
        (120, "ZZZ", "4444444"),
        (-3, "BRA", "3333333"),
        (3, "USA", "2222222")
    ]
    #  sorted here only operates on the first field of the tuple?
    #  breaking ties by the next field ?
    for passport in sorted(traveler_ids):
        #  here % can handle tuples directly
        print("%d/%s/%s"%passport)


def tuple_unpacking():
    #  swapping the values of two variables without using a temp variable
    a = 3
    b = 4
    print(a,b)
    a, b = b, a
    print(a, b)

    #  prefixing argument with star
    arguments = (20, 8)
    quotient, remainder = divmod(*arguments)
    print(quotient, remainder)


def excess_items():
    #  use *args t ograb arbitrary excess arguments
    for k in range(5, 1, -1):
        a, b, *rest = range(k)
        print(type(rest), rest)

    #  parallel assignment: * can appear anywhere, but only once
    for k in range(5, 1, -1):
        a, *rest, b = range(k)
        print(type(rest), rest)
    
def named_tuple():
    from collections import namedtuple
    #  less memory than regular object because they don't store attributes in
    #  a per-instnace __dict__
    #  same memroy as regular tuple, because the field names are stored in the class
    City = namedtuple('City', 'name country population coordinates')
    tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    la = City('LA', 'USA', 100.00, 3)
    print(tokyo)
    print(la)
    #  As can be seen, Python interpreter won't know/care the type of coordinates
    print(tokyo.coordinates)
    print(la.country)
    #  methods
    ny_param = ('New York', 'USA', 3000.00, (200,300))
    ny_city = City(*ny_param)
    ny_dict = ny_city._asdict()
    print(ny_dict)
    
    
    

#tuple_as_record()
#tuple_unpacking()
#excess_items()
named_tuple()
