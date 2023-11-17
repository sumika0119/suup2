# クラスの定義

class Car:
    """車クラス"""
    country = 'Japan'
    year = 2019
    name = 'Prius' # プロパティ
    def print_name(self):
        print('print_name実行') 
        print(self.name) # プロパティを呼び出す

my_car = Car() #インスタンス化（車クラスを呼び出す）
print(my_car.year)
my_car.print_name() # print_nameというメソッドを実行することができる
list_a = ['apple', 'banana', Car()]
# second_car = list_a[2]()
# second_car.print_name()
list_a[2].print_name()
help(Car) # 車クラスの文字列を見ることができる # スペースを押すと先に進める。qでhelpを閉じる