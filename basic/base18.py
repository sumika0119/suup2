# for 

for i in range(10):
    print(i)

for _ in range(100): #_の中に100格納
    print('A') # Aが100回表示される

for i in range(2,20,3): # 2から19まで3ことばし
    print(i)

# sample = ['John', 'Paul', 'George', 'Ringo']
sample = ('John', 'Paul', 'George', 'Ringo') # タプルでもリストでも辞書でもできる
for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'Man'
}
for h in human:
    print(h) # keyのみ取り出せる（Name,Age,gender)
    print(h,human.get(h)) # keyとkeyに対応した値を取り出せる