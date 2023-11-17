# クラスの多重継承

class ClassA:

    def __init__(self, name):
        self.a_name = name

    def print_a(self):
        print('ClassAのメソッドを実行')
        print('a = {}'.format(self.a_name))

    def print_hi(self):
        print('A hi')


class ClassB:

    def __init__(self, name):
        self.b_name = name

    def print_b(self):
        print('ClassBのメソッドを実行')
        print('b = {}'.format(self.b_name))

    def print_hi(self):
        print('B hi')

class NewClass(ClassA, ClassB):

    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name) # ClassAの初期化
        ClassB.__init__(self, b_name) # ClassBの初期化
        self.name = name
    
    def print_new_name(self): # 多重継承では新たにメソッド（クラスの中で定義した関数）定義することもできる
        print('name = {}'.format(self.name))

    def print_hi(self): # オーバーライド→親クラスのメソッドを上書きして新たに定義
        ClassA.print_hi(self) # クラスの中にあるメソッドを呼び出すときは、クラス名．メソッド名
        ClassB.print_hi(self)
        print('NewClass hi')

sample = NewClass('AName', 'BName', 'New Class Name')

sample.print_a() # ClassAが持っているメソッドを実行
sample.print_b() # ClassBが持っているメソッドを実行
sample.print_new_name() # NewClassが持っているメソッドを実行
sample.print_hi() # NewClassがオーバーライドしたprint_hiという関数を実行