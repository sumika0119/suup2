# Private変数→print(human.__name)としてもクラスの外からは表示されない。表示するには、クラス内からprivate変数にアクセスできる変数を定義

class Human:

    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name #private変数
        self.__age = age #private変数

    def print_msg(self):
        print('name = {}, age = {}'.format(self.__name, self.__age))# クラス内からprivate変数にアクセスできる

human = Human('Taro', 15)
# print(human.__name) #インスタンス変数を指定してアクセスするとTaroと表示されるがprivate変数にするとクラスの外からは表示されない
# print(human._Human__name) # クラスの外からアクセス（表示）できる。基本的に使わない
human.print_msg()#private変数にアクセスできる