# クラスの継承

class Person: # 親クラス

    def __init__(self, name, age): #親クラスが持つプロパティ（name, age）
        self.name = name
        self.age = age

    def greeting(self): # メソッドgreeting
        print('hello {}'.format(self.name))

    def say_age(self): # メソッドsay_age
        print('{} years old'.format(self.age))

class Employee(Person): # 子クラス # Personの機能を継承

    def __init__(self, name, age, number): #self.name,self.nameあるいはgreeting,say_ageを継承されている
        super().__init__(name, age) # super()で親クラスを呼び出し、__init__でname,nameを初期化
        self.number = number # numberを子クラスで初期化

    def say_number(self):
        print('My number is = {}'.format(self.number))

    def greeting(self): # オーバーライド→親クラスのメソッドを上書きして新たに定義
        super().greeting()
        print('I\'m employee phone_number = {}'.format(self.number))

    # def greeting(self, age): # オーバーロード（pythonではできない）→引数が違っても24行目の関数を引き継いでしまう
        # print('オーバーロード')
man = Employee('Tonegawa', 45, '00011111111') 
man.greeting() # オーバーライドした24行目を実行　#24行目で親クラスの9行目を呼び出し、その後26行目を実行
man.say_age() # 親クラスの12行目を実行
man.say_number() # 子クラスの21行目を実行