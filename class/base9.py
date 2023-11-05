# ポリモーフィズム

from abc import abstractmethod, ABCMeta # まずabstractクラスをインポートする

class Human(metaclass=ABCMeta): #親クラスを定義。抽象クラスをmetaclass=ABCMetaとして指定

    def __init__(self, name):
        self.name = name

    @abstractmethod #抽象メソッド
    def say_something(self):
        pass # 中身を定義しない場合

    def say_name(self):
        print(self.name) # nameというインスタンスメソッドを表示するメソッドとする

class Woman(Human): #Humanクラスを継承
    
    def say_something(self):
        print('女性：名まえは={}'.format(self.name))

class Man(Human): #Humanクラスを継承
    
    def say_something(self):
        print('男性：名まえは={}'.format(self.name))


#ポリモーフィズム（プログラムを書いている時はどのクラスになるかわからない実行するときに分かる。）
num = input('0か1を表示してください')
if num == '0':
    human = Man('Taro')#Manクラスが格納。24行目が実行
elif num == '1':
    human = Woman('Hanako')#Womanクラスが格納。20行目が実行
else:
    print('入力が間違っています')
human.say_something()# say_somethingの呼び出し（ポリモーフィズム）
human = Woman('Hanako') #エラーが起こる。class Womanの中で@abstractmethodを定義していない。親クラスから継承した子クラスは必ず抽象メソッドを定義しないといけない(19行目)
