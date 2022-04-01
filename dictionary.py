# 辞書を作成. 今回は(果物の名前:果物の数)の辞書を作った.
dict1 = {"apple":1, "banana":3, "orange":2}

# dict1 の要素にアクセス.
print(dict1["apple"])
print("-------------------------")

# dict1 に新しい要素を追加.
dict1["pair"]= 4
print(dict1["pair"])
print("-------------------------")

# dict1 の各要素を表示.
for dict in dict1.items():
    print(dict)
print("-------------------------")

# 果物の名前順で dict1 をソート.
print(sorted(dict1.items(), key = lambda x : x[0]))
print("-------------------------")

# 果物の数の順で dict1 をソート.
print(sorted(dict1.items(), key = lambda x : x[1]))
