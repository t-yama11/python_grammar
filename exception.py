"""
例外処理の書き方
try:
    例外の起こる可能性のある処理
except 例外:
    例外が起きた際の処理
else:
    例外が起きなかった場合の処理
finally:
    例外発生の有無に関係なく行う処理
"""
class TypeIntError(TypeError):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'{__class__.__name__} : {self.num}は整数ではありません.'


def main():
    a = 2
    b = 3

    val = a/b
    if not isinstance(val, int):
        raise TypeIntError(val)
    
    # 例外が発生しない場合, 計算結果を表示する.
    print(val)


if __name__ == "__main__":

    # a/bの結果に対する例外処理
    try:
        main()
    except ZeroDivisionError as e:
        print(e)
    except TypeIntError as e:
        print(e)
    finally:
        print("計算を行いました.")