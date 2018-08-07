import numpy as np

def encode(x):
    y = np.zeros(10)
    np.put(y, x, 1)
    return y

list = [[1,2,4],[4,5,6],[77,8,8]]
list2 = a = np.arange(5)
print(encode(6))
print(list2)
