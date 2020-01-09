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
    

#tuple_as_record()
tuple_unpacking()
