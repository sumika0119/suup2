# コンストラクタ（インスタンスを作成する際に呼び出す）、デストラクタ（インスタンスを削除する際に呼び出す）

class SampleClass:

    def __init__(self, msg, name=None): # コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg # インスタンス変数
        self.name = name # インスタンス変数

    def __del__(self):
        print('デストラクタが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)
    
var_1 = SampleClass('Hello', 'Jiro') # 6行目が実行される
var_1.print_msg()
var_1.print_name()
del var_1


