# raise 例外自作

class MyException(Exception): #自分でクラスを作ることもできる（作ったクラス名が表示される）
    pass

def devide(a, b):
    if b == 0:
        raise MyException('0では割り切れません') # raise:例外を返す
    else:
        return a / b
    
try:
    c = devide(10, 0)
except Exception as e: # Exception:例外を自作
    print(e, type(e))
