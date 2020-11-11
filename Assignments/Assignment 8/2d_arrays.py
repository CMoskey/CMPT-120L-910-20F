def sum_2d_array(two_d_array):
    import numpy as np

    List = np.array(two_d_array,dtype=object)
    
  
    res = np.sum(List, 0) 
    return res

if __name__ == "__main__":
    two_d_array=[[2, 6, 7, 98, 3, 434, 2, 4, 2],
                [-12, 3, 454, 6778, 234, -999, 2543, -2323],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [],
                [1000000000000000],
                [1],
                [0]]
    answers = sum_2d_array(two_d_array)
    
    print(answers)
