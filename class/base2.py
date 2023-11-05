# インスタンス変数（インスタンスごとに別々に利用する変数）、クラス変数（オブジェクト同士で共有することができる変数）

class SampleA():
    class_val = 'class val' # クラス変数

    def set_val(self):
        self.instance_val = 'instance val' # インスタンス変数は関数の中で定義

    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val)) # クラス変数とインスタンス変数をprint_valの中で呼び出せる
        print('インスタンス変数 = {}'.format(self.instance_val)) # クラス変数とインスタンス変数をprint_valの中で呼び出せる

instance_a = SampleA() # インスタンス化
instance_a.set_val() # 6行目のset_valが呼び出されてinstance_valにinstance_valが設定される。
print(instance_a.instance_val) # instance_valを呼び出す
instance_a.print_val() #クラス変数とインスタンス変数をprint_valというメソッドを呼んで表示できる
print(SampleA.class_val) # class_valを呼び出す
print(instance_a.__class__.class_val) # クラス変数 # class_valを呼び出す
instance_b = SampleA() # インスタンス化
instance_b.set_val() #クラス変数はclass valだと呼び出す
instance_b.print_val()
instance_a.__class__.class_val = 'class val 2'
instance_b.print_val() # クラス変数はインスタンス間で共有されるのでむやみに書き換えない

print('*'*100)
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val)) # クラス変数はインスタンス間で同じ物を指すようになるのでコードも同じ数になる