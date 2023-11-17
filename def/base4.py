# inner関数（用途：外の関数の外からアクセスできないような関数を作成、関数の中で同じ処理が何度も発生する場合に一つにまとめる、デコレータ関数を作成）
#ノンローカル関数

def outer(): #ノンローカル関数を定義しないとouterとinnnerでそれぞれの値が表示
    outer_value = '外側の変数'
    def inner():
        nonlocal outer_value #ノンローカルを入れると内側の変数に外側の変数が書き換わる
        outer_value ='内側の変数'
        print('inner: outer_value = {}. id = {}'.format(outer_value,id(outer_value)))
    inner() #ここを書かないいとAが表示されない
    print('outer: outer_value = {}. id = {}'.format(outer_value,id(outer_value)))

outer()