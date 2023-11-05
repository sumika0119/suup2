# continue,break,else

for i in range(10):
    if i == 3:
        continue # break(3に前に終わる) continue(3だけ飛ばされる)
    print(i)
else:
    print('ループ処理終了')

num = 0
while num < 10:
    if num == 5:
        num += 1 # この文を書かないとcontinueの後（5を飛ばした後）+1がされないので無限ループになる
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1 # この文を入れないとbreakの後num = 0でずっと0が出る
else:
    print('whileループ終了')