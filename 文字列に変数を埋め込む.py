"""
目標: 文字列の結合の仕方について勉強.
背景: 自分の作成したソースコードの中で, 可読性の悪い書き方が存在したため.
"""

# + を用いて文字列を結合.
def sample1(name):
    greeting = 'Hello, My name is ' + name
    print(greeting)

# formatを用いて文字列を結合.
def sample2(name):
    greeting = 'Hello, My name is {0}'.format(name)
    print(greeting)

# f文字列を用いて文字列を結合.
def sample3(name):
    greeting = f'Hello, My name is {name}'
    print(greeting)

if __name__ == "__main__":
    name = 'Tom'
    
    sample1(name)
    sample2(name)
    sample3(name)