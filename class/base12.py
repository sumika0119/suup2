# setter getter (カプセル化の方法その２)

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self): # getter
        print('getter name が呼ばれました')
        return self.__name
    
    @property
    def age(self):
        print('getter age が呼ばれました')
        return self.__age
    
    @name.setter
    def name(self, name):
        print('setter name が呼ばれました')
        self.__name = name

    @name.setter
    def age(self, age):
        print('setter age が呼ばれました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age

human = Human('Koichi', 22)
human.name = 'Makoto' # 左側に.nameがあるので、代入しようとすると20行目が呼ばれる。private変数__nameにMaokotoが代入される
print(human.name) 
human.age = -1 #25行目が呼ばれ、0未満なので「0以上の値を設定してください」と実行される
print(human.age)

