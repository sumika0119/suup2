# setter, getter→カプセル化（クラスの外部から変数が見えないようにする）をする際にsetterとgetterを定義してsetterとgetterを利用しないとアクセスできないようにする。

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        print('getter name を呼び出しました')
        return self.__name

    def get_age(self):
        print('getter age を呼び出しました')
        return self.__age
    
    def set_name(self, name): #値を書き換える
        print('setter name を呼び出しました')
        self.__name = name #__nameのpraivete変数を書き換えることができる

    def set_age(self, age):
        print('setter age を呼び出しました')
        self.__age = age

    name = property(get_name, set_name) # nameを指定するとget_name, set_nameが呼び出される
    age = property(get_age, set_age) #ageを指定するとget_age, set_ageが呼び出される

    def print_msg(self):
        print(self.name, self.age)

human = Human('Taro', 15)
human.name = 'Jiro' # （propertyを作成すると）__nameが書き換わり、インスタンスにアクセスしているように見えて、実際はset_nameを呼び出している
# 18行目が呼ばれる #左側に.name（=で値を代入）する場合はset_nameが呼ばれる
human.age = 18 #(propertyを作成すると)__ageが書き換わり、実際はset_ageを呼び出し22行目が呼ばれる

# print(human.name) #getterが呼び出される。10,11行目が返される
name = human.name # 右側に.nameもしくはprintでかくと（値の参照になるので）get_nameが呼ばれる
# print(human.age) # getterが呼び出される。14,15行目が返される
age = human.age
print(name, age)