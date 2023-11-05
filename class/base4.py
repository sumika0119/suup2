# インスタンスメソッド、クラスメソッド、スタティックメソッド

class Human:

    class_name = 'Human' # クラス変数

    def __init__(self, name, age): # コンストラクタ
        self.name = name
        self.age = age

    def print_name_age(self): #インスタンスメソッド（第1引数にselfを取るが呼び出し時には第2引数以降を渡す)
        print('インスタンスメソッド実行')
        print('name = {}, age = {}'.format(self.name, self.age))

    @classmethod # （これを作ることでクラスメソッドとして定義することができる）
    def print_class_name(cls, msg): # クラスメソッド(第1引数にclsを取る。clsにはクラス自身が入る)
        print('クラスメソッド実行')
        print(cls.class_name) #クラス変数にアクセス
        print(msg)

    @staticmethod
    def print_msg(msg): # スタティックメソッド(第1引数にこれを取るという決まりはない)
        print('スタティックメソッド実行')
        print(msg)


Human.print_class_name('こんにちは') # クラスメソッド（インスタンス化せずにクラスのまま直接実行できる。ただしインスタンス変数やコンストラクタの変数を呼び出せない）が実行される
man = Human('桜木', 18) # インスタンス変数が初期化される（self.name self.age）
man.print_name_age() # インスタンスメソッド（インスタンス化して、インスタンス変数に値を設定した後実行するメソッド）を実行
man.print_msg('hello static') #クラスから直接アクセスすることもできる（31行目でも○）
Human.print_msg('hello static') #クラスから直接アクセスすることもできる
# クラス変数やインスタンス変数にアクセスする必要がないときはスタティックメソッドを使う