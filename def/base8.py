# 高階関数

# def print_hello():
#     print('hello')

# def print_goodbye():
#     print('goodbye')

# var = ['AA', 'BB', print_hello, print_goodbye]
# var[2]()
# var[3]()

def print_world(msg): # ()内は引数
    print('{}world'.format(msg))

def print_konnichiwa():
    print('こんにちは')

def print_hello(func):
    func('hello')
    return print_konnichiwa

var = print_hello(print_world) 
var()
# print_helloが呼び出されてprint_helloに引数funcで実行。引数msgにhelloが渡って14行目が実行される。21行目にprit_konnichiwaが返ってきているのでvarに格納される。23行目でバーが実行されてこんにちはが表示される。