# セット

set_a = {'a', 'b', 'c', 'd', 'a', 12} # { } の中に[ ]を入れることはできない。エラーになる
print(set_a)
print('e' in set_a) # セットの要素確認（False True）
print('a' in set_a)
print('a' not in set_a) # 存在しないときTrue

# add , remove , discard , pop , clear
set_a.add('A') # 要素の追加
print(set_a)

set_a.remove('a') # 要素の削除。存在しないとエラーになる
print(set_a)

set_a.discard(13) # 要素の削除。存在しなくてもエラーにならない。
print(set_a)

val = set_a.pop() # 任意の要素の取り出し。取り出した値以外の値は{ }中に表示
print(val, set_a)

set_a.clear() # セットを空にする
print(set_a)

