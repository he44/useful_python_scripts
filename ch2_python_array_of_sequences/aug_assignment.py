def corner_case():
    t = (1, 2, [30, 40])
    t[2] += [50, 60]
    #  will get an error: 
    #  TypeError: 'tuple' object does not support item assignment
    #  but if we print out t, it will become
    #  (1, 2, [30, 40, 50, 60])
    #  might not be good to put mutable objects in tuples


corner_case()
