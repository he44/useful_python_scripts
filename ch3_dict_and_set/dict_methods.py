def missing_key():
    a = dict(USA=1, CHINA=96, INDIA=91)
    print(a)

    #  get(key, default) method is similar to [],
    #  but return "default" is key missing
    #  dict is not changed
    val = a.get('JAPAN', 81)
    print(val)
    print(a)
    
    #  setdefault(key, default) returns [key] if key in dict
    #  if not, return default and set [key] = default in dict
    val = a.setdefault('JAPAN', 81)
    print(val)
    print(a)

    val = a.setdefault('JAPAN', 82)
    print(val)
    print(a)

missing_key()
