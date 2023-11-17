# デコレータ関数↓
# @関数名と関数の前に付けることでできる。
# 関数オブジェクトを引数にとって引数にとった関数に実行時に変更を加える。
# 関数間である処理を共通に利用したい場合に用いられる

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(args[0]) # 間数間である処理を共通に利用したい＊の前に０
        if args[0] == 1:
            return 1
        print('*' * 100) # func_aを実行に＊
        func(*args, **kwargs)
        print('*' * 100)
    return wrapper
    
@my_decorator # 関数間である処理を共通に利用したい場合に用いられる
def func_a(*args, **kwargs):
    print('func_aを実行')
    print(args)

@my_decorator # 関数間である処理を共通に利用したい場合に用いられる
def func_b(*args, **kwargs):
    print('func_bを実行')
    print(args)

func_a(1, 2, 3)
func_b(1, 2, 3)