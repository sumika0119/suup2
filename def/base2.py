# デフォルト値、可変数引数、複数の返り値


def sample (arg1, arg2=100): # デフォルト値: arg=xx 実行する際に第2引数をしていしなければ100と表示される
    print(arg1, arg2)

# sample(200, 300) #sample(200)とすると、200 100と表示される

def spam(arg1, *arg2): # *は可変長タプルになる（引数の数を変えられるタプル）# 可変長引数を設定するときは最後の引数に設定する。可変長引数は１つのみ設定可
    print("arga = {}, arg2 = {}".format(arg1, arg2))
    print(type(arg2))

spam(1,2,3,4,5)

def spam_2(arg1, **arg2): # *は可変長辞書になる（引数の数を変えられる辞書型）
    print("arga = {}, arg2 = {}".format(arg1, arg2))
    print(type(arg2))

spam_2(3, name='Taro', age=20)

def spam_3(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)

spam_3(1,2,3,4,5,name='Taro', age=15)

def sample_2():
    return 1, 2 # return 複数の返り値（関数から複数の返り値を返す）

a,b = sample_2() # 呼び出すときは変数を複数用意（a, b）
print(a, b)