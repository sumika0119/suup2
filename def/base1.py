# 関数

def print_hello(): #関数の定義def
    print('Hello World')

print_hello() #実行される。3,4行目を呼び出している

def num_max(a: int, b: int):
    print('a = {}, b = {}'.format(a, b))
    if a > b:
        return a # return 返り値呼び出している
    else:
        return b
print(num_max(b = 100, a = 20)) # 変数を直接指定することもできる。変数の順番を気にせず入力できる
print(num_max('20', '30')) # 型を指定できる。()をかくと（a: int, b: int）とヒントが表示される（あくまでヒント）