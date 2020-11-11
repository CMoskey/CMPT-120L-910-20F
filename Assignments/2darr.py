import numpy as np

two_d_array([[2, 6, 7, 98, 3, 434, 2, 4, 2],
    [-12, 3, 454, 6778, 234, -999, 2543, -2323],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [],
    [1000000000000000],
    [1],
    [0]])
answers = np.sum(two_d_array,axis=1)
print(answers)