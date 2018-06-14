import numpy as np
inp = np.arange(100).reshape(10,10) #define the range of the matrix and reshape them
print(inp)

for i in range(10):
    # for each row of the matrix print maximum and minimum value
    print("The max and min of row {} is {}, {}".format(i, max(inp[i]), min(inp[i])))
