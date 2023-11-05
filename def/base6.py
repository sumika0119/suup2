# サブジェネレーター

def sub_sub_generator():
    yield "Sub Subのyield" # yield 処理を停止してメインに値を返す
    return "sub sub のreturn" # return呼び出し元に値を返す

def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator() # yield fromサブジェネレーターの呼び出し
    print("sub res = {}".format(res))
    return "subのreturn"

def generator():
    yield "generatorのyield"
    res = yield from sub_generator()
    print('gen res = {}'.format(res))
    return 'generatorのreturn'

gen = generator()
print(next(gen)) #14行目
print(next(gen)) #14行目から処理がスタート。15行目→sub_generatorに移動 8行目
print(next(gen)) #9行目→sub_sub_generatorに移動 4行目
print(next(gen)) #5行目→sub subのreturnを呼び出し元に返す。10行目（sub_sub_generatorの呼び出し元なのでsub_generator）
print(next(gen)) #11行目→subのreturnを呼び出し元に返す。（generator）16行目