# enumerate, zip, while

fruits = ['grape','Pine', 'Apple']

for index,value in enumerate(fruits): # index（数）,value（値）両方取り出せる
    print('index = {}'.format(index))
    print('value = {}'.format(value))

classA = ['Taro', 'Haruko', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Tato']

for A, B in zip(classA, classB): #zip ２つ配列の中の値を取り出す（ループする）
    print('classA = {}'.format(A))
    print('classB = {}'.format(B))


count  = 0
while count < 10: # countが10より小さい場合は中の処理を実行する
    print(count)
    count += 1