import numpy as np

"""
all()とany()の使い方を勉強する.
all()は全ての要素がある条件を満たす場合, Trueとなる.
反対にany()は少なくとも1つの要素がある条件を満たす場合, Trueとなる.
"""

def sample_any():
    array = np.array([0, -1, 2])
    judge = False
    for a in array:
        if a >= 0:
            judge = True
    print(judge) # Trueと表示.

def sample_all():
    array = np.array([0, -1, 2])
    judge = True
    for a in array:
        if a < 0:
            judge = False
    print(judge) # Falseと表示.

def test1_any():
    array = np.array([0, -1, 2])
    judge = any(map(lambda item: item>=0, array)) # map(lambda item: item>=0, array)ってどういう意味?
    print(judge) # Trueと表示.

def test1_all():
    array = np.array([0, -1, 2])
    judge = all(map(lambda item: item>=0, array))
    print(judge) # Falseと表示. 

if __name__ == "__main__":
    sample_any()
    sample_all()
    test1_any()
    test1_all()
