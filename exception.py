"""
例外処理の書き方
try:
    例外の起こる可能性のある処理
except 例外:
    例外が起きた際の処理
"""

class TypeIntError(TypeError):
    print("整数ではありません.")
    pass

if __name__ == "__main__":
    a = 2
    b = 3

    # a/bの結果に対する例外処理
    try:
        val = a/b
    except ZeroDivisionError as e:
        print(e, f"{a}/{b}")
    else:
        if isinstance(val, int):
            print(val)
        else:
            TypeIntError(f"{val}は整数ではありません.")