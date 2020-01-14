from array import array
#  typecode
#  'b': signed char
#  'd': float (?)
# floats = array('d', (random() for i in range(10**7)))
#  can be save/loaded via "tofile" and "savefile"
#  fast (much faster than saving/reading using txt files)
#  pickle: also fast, but can handle almost all data types

from collections import deque
dq = deque(range(10), maxlen=10)
#  rotate(n), if n > 0, take the right most n elements, append to left
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
#  when maxlen is reached, appending elements will pop out the first element on the other end
dq.appendleft(11)
print(dq)
dq.append(12)
print(dq)
#  adding more than one elements, using extend
dq.extend([12,13])
print(dq)
