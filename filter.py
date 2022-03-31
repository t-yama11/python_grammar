"""
filter関数の使い方について勉強する.

使い方
filter(関数, オブジェクト(リスト, タプルなど))

オブジェクトが tuple である場合, 要素の追加や変更はできない為(同じidの変数は変更不可能), filter関数を使用する.
オブジェクトが list である場合, 内包表記でも良い. 内包表記は関数の形が簡単なもの(各要素を2枚するなど)
に限定する方が望ましい.
"""

def sample1():
    """
    値が4以上のリストの要素を削除する.
    """
    list1 = [1,2,3,4,5]
    print(list1[:3])

def sample2():
    def func(element):
        return element <= 3

    """
    値が4以上のリストの要素を削除する. filter関数を使用した書き方.
    """
    list1 = [1,2,3,4,5]
    list1 = list(filter(func, list1))
    print(list1)

def sample3():
    """
    リストの各要素を2枚する. 内包表記を使用した書き方.
    """
    list1 = [1,2,3,4,5]
    list1 = [e for e in list1 if e <= 3]
    print(list1)

def sample4():
    tuple1 = (1,2,3,4,5)
    tuple1 = tuple(filter(lambda e: e<=3, tuple1))
    print(tuple1)

if __name__ == "__main__":
    sample1()
    sample2()
    sample3()
    sample4()
