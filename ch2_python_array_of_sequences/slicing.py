def slicing():
    s = 'bicycle'
    print(s[::3])  #  every third strating from index 0 --> bye
    print(s[::-1]) #  every previous item from index -1 --> elcycib (reversed)
    print(s[::-2]) #  --> eccb


def md_slicing():
    import numpy as np
    a = np.arange(9).reshape(3,3)
    print(a)
    #  these two operations are equivalent
    b = a[0, ...]
    c = a[0, :]
    print(b)
    print(c)

def sequence():
    l = [1,2,3]
    print(l)
    b = l * 5
    #  this is a new object
    #  so changing b or l won't affect each other
    print(b)
    b[0] = 0
    print(b)
    print(l)
    l[2] = 2
    print(b)
    print(l)

def reference():
    #  correct way to build lists of lists
    board = [['_'] * 3 for i in range(3)]
    print(board)
    board[1][2] = 'X'
    print(board)

    #  wrong way to build lists of lists
    board = [['_'] * 3 ] * 3 # this is just a list of three references to the same list
    print(board)
    #  each list will be changed
    board[1][2] = 'O'
    print(board)
    
    

#slicing()
#md_slicing()
#sequence()
reference()
