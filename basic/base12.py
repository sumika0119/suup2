# タプル

fruit = ('apple', 'banana', 'lemon')

print(fruit)
print(type(fruit))
print(fruit[0])
# fruit[1] = 'grape'
fruit = fruit+ ('grape',) # タプルの追加
print(fruit)

list_fruit = ['apple', 'banana']
fruit = tuple(list_fruit) # リストのタプルへの変換
print(fruit)
print(fruit.count('apple')) # カウント（appleが何個あるか）
print(fruit.index('banana')) # 検索（インデックスでどこにあるか）

pos = (135,35) # 東経135度　北緯35度

countries ={pos: 'Japan'} # 対応するのは日本

print(countries.get((135,35)))