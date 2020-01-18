def create_dict():
    a = dict(one = 1, two = 2, three = 3) # this one is neat
    b = {"one":1, "two":2, "three":3} # i know this one
    #  isn't c and d just swapping out the zip to a list of tuple
    c = dict(zip(['one', 'two', 'three'], [1,2,3]))
    d = dict([('two',2), ('one', 1), ('three',3)])
    #  if I can do b, why e?
    e = dict({'three':3, 'one':1, 'two':2})
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(a==e)

def dict_comprehension():
    DIAL_CODES = [(86, 'China'), (91, 'India'), (1, 'USA')]
    #  we can also use if statement to filter out stuff in dict comprehension, cool
    country_code = {country: code for code, country in DIAL_CODES if code < 90}
    print(country_code)


dict_comprehension()
create_dict()
