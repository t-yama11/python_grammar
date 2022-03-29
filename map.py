"""
map関数の使い方について勉強する.

使い方
map(関数, オブジェクト(リスト, タプルなど))

オブジェクトが tuple である場合, 要素の追加や変更はできない為(同じidの変数は変更不可能), map関数を使用する.
オブジェクトが list である場合, 内包表記でも良い. 内包表記は関数の形が簡単なもの(各要素を2枚するなど)
に限定する方が望ましい.
"""

def sample1():
    """
    リストの各要素を2枚する.
    """
    list1 = [1,2,3,4,5]
    for i,e in enumerate(list1):
        list1[i] = e*2

    print(list1)

def sample2():
    def multi(element):
        return 2*element

    """
    リストの各要素を2枚する. map関数を使用した書き方.
    """
    list1 = [1,2,3,4,5]
    list1 = list(map(multi, list1))
    print(list1)

def sample3():
    """
    リストの各要素を2枚する. 内包表記を使用した書き方.
    """
    list1 = [1,2,3,4,5]
    list1 = [e*2 for e in list1]
    print(list1)

def sample4():
    tuple1 = (1,2,3,4,5)
    tuple1 = tuple(map(lambda e: e*2, tuple1))
    print(tuple1)

if __name__ == "__main__":
    sample1()
    sample2()
    sample3()
    sample4()
