import cv2
import numpy as np

"""
cv2.convertPointsToHomogeneous()は,
・引数の配列の次元数が2.
・行数,列数共に2以上.
"""

def assert_(func):
    try:
        print(func())
    except Exception:
        print("例外が発生しました.")

def two_dims_array():
    array = np.float32([[0,1], 
                        [2,3]])
    array_hom = cv2.convertPointsToHomogeneous(array)
    return array_hom

def two_dims_array_2_3():
    array = np.float32([[0,1,2],
                        [2,3,4]])
    array_hom = cv2.convertPointsToHomogeneous(array)
    return array_hom

def two_dims_array_3_2():
    array = np.float32([[0,1],
                        [2,3],
                        [4,5]])
    array_hom = cv2.convertPointsToHomogeneous(array)
    return array_hom

def two_dims_array_3_3():
    array = np.float32([[0,1,10],
                        [2,3,11],
                        [4,5,12]])
    array_hom = cv2.convertPointsToHomogeneous(array)
    return array_hom

def two_dims_array_3_1():
    array = np.float32([[3],
                        [2],
                        [1]])
    array_hom = cv2.convertPointsToHomogeneous(array)
    return array_hom

def one_dims_array_3():
    array = np.float32([0,1,2])
    array_hom = cv2.convertPointsToHomogeneous(array)
    return array_hom


if __name__ == "__main__":
    print("1: -----------------------------------")
    assert_(two_dims_array) # 次元数が2
    
    print("2: -----------------------------------")
    assert_(two_dims_array_2_3) #次元数が2,行数と列数が共に2以上. 

    print("3: -----------------------------------")
    assert_(two_dims_array_3_2) #次元数が2,行数と列数が共に2以上. 

    print("4: -----------------------------------")
    assert_(two_dims_array_3_3) #次元数が2,行数と列数が共に2以上. 

    print("5: -----------------------------------")
    assert_(two_dims_array_3_1) #次元数が2,行数と列数が共に2以上でない.

    print("6: -----------------------------------")
    assert_(one_dims_array_3) #次元数が1,行数と列数が共に2以上でない.
