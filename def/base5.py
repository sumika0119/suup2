# ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max): # ループ分 nにmax の値を代入
        try:
            x = yield n 
            print('x = {}'.format(x))
            print('yield実行')
        except ValueError as e:
            print('throwを実行しました')

gen = generator(10) # 数字を1にするとnextが2回あるのに、m=0しかできないのでエラーが発生
next(gen) # 処理を実行するための関数next
gen.send(100) #send 値を送出
# gen.throw(ValueError('Invalid Value')) # 例外を発生させる
# gen.close() #終了させる
next(gen)
# n = next(gen) # next 実行　n=0出実行される
# print('n = {}'.format(n))
# n = next(gen)
# print('n = {}'.format(n)) # n=1で実行される。ループされるのでnがyieldに戻ってyieldと表示される
# for x in gen:# nextを毎回書くのは大変→ループ文を書く
#     print('x = {}'.format(x))

# send の場合は x = yield n（xをつける）

