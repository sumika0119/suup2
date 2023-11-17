# グローバル変数

def printAnimal():
    global animal # 関数内と関数外のanimalが同じになりidも同じ場所になる
    animal = 'Cat'
    print('関数内animal = {}, id = {}'.format(animal, id(animal))) # id 変数が指しているメモリ上の場所

animal = 'Dog'
printAnimal()
print('関数内animal = {}, id = {}'.format(animal, id(animal)))
