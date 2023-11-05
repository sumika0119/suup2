#辞書型のメソッド


car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_car = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}

car.update(tmp_car) #値の追加更新（updateメソッドを使用する方法'
print(car)


car['city'] = 'Toyota-shi' #値の書き換え（直接書き換える方法）
car['year'] =  2017
print(car)

value = car.popitem() #最後に追加した要素の取り出し
print(car)
print(value)

value = car.pop('model') #キーを指定して値を取り出し
print(car)
print(value)

car.clear() #辞書の中身のクリア
print(car)

del car #変数の中身そのものを削除
print(car)