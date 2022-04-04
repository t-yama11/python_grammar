"""
例外処理の書き方
try:
    例外の起こる可能性のある処理
except 例外:
    例外が起きた際の処理
"""

if __name__ == "__main__":
    # ゼロ割の例外処理
    try:
        print(1/0)
    except ZeroDivisionError:
        print("ゼロで除算しています.")