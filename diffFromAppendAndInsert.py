import numpy as np
from mesureProcessingTime import measure_processing_time


"""
np.append()とnp.insert()の処理時間を比較した.
ndarray型配列 add_array の要素を一つずつ, ndarray型配列
init_arrayの先頭に追加する処理を用いて処理時間の比較を行なった.
結果は np.append()の方が np.insert()よりも処理時間が約2倍速かった.
※ for文を用いないソースコードの方が処理時間の短縮に繋がる.

結果例:
init_array = np.array([0]), add_array = np.array([i for i in range(1,3)])のとき,
testNpAppend : 0.0004970730000000145 [s]
testNpInsert : 0.00021079099999998796 [s]

init_array = np.array([0]), add_array = np.array([i for i in range(1,10)])のとき,
testNpAppend : 0.00006965099999997615 [s]
testNpInsert : 0.00019168699999999594 [s]

init_array = np.array([0]), add_array = np.array([i for i in range(1,100)])のとき,
testNpAppend : 0.0005248539999999913 [s]
testNpInsert : 0.001873893999999987 [s]

init_array = np.array([0]), add_array = np.array([i for i in range(1,1000)])のとき,
testNpAppend : 0.004903023000000006 [s]
testNpInsert : 0.014895465999999996 [s]

init_array = np.array([0]), add_array = np.array([i for i in range(1,10000)])のとき,
testNpAppend : 0.06616702199999999 [s]
testNpInsert : 0.130443354 [s]

init_array = np.array([0]), add_array = np.array([i for i in range(1,100000)])のとき,
testNpAppend : 1.9928096729999998 [s]
testNpInsert : 2.876464155 [s]

init_array = np.array([0]), add_array = np.array([i for i in range(1,200000)])のとき,
testNpAppend : 7.078716377 [s]
testNpInsert : 8.610616481 [s]
"""
@measure_processing_time
def testNpAppend(init_array, add_array):
    for a in add_array:
        init_array = np.append(a, init_array)
    # print(init_array)

@measure_processing_time
def testNpInsert(init_array, add_array):
    for a in add_array:
        init_array = np.insert(init_array, 0, a)
    # print(init_array)


if __name__ == "__main__":
    init_array = np.array([0])
    add_array = np.array([i for i in range(1,10)])
    testNpAppend(init_array, add_array)
    testNpInsert(init_array, add_array)