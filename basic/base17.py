# all, any

if all((True, 10<20, 'a' == 'a')): # allはオブジェクトの中が全てTtueの場合に処理する
    print('allの中の処理')

if any((10<20, 10<5, 'a' == 'b')): # anyはオブジェクトが一部Trueの場合に処理
    print('anyの中の処理')