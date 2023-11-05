# 演習５

from abc import abstractmethod, ABCMeta

class Animals(metaclass=ABCMeta):

    @abstractmethod #抽象メソッド(具体的な処理は継承したクラスに記述する)複数のクラスに対して強制的に共通機能を持たせる
    def speak(self): #抽象メソッド→親クラスで必ず定義。子クラスで必ずオーバーライドする
        pass

class Dog(Animals): # Animalsを継承
    
    def speak(self): # speakをオーバーライド
        print('わん')

class Cat(Animals):

    def speak(self):
        print('にゃー')

class Sheep(Animals):

    def speak(self):
        print('めー')

class Other(Animals):

    def speak(self):
        print('そんな動物いない')

number = input('好きな動物は？ 1:犬、2:猫、3:羊')

if number == '1':
    animal = Dog()
elif number == '2':
    animal = Cat()
elif number == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak() # speakの呼び出し（ポリモーフィズム）