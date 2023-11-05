num = 10 
print(type(num)) # numの型を出力してください

num_str = str(num) # numを文字列に変換する
num_list = [num_str,'20','30'] # num_listにnum_strと'20','30'を入れる（全部文字列）
print('num_list = {}' .format(num_list))

num_list.append('40') # 新たな要素を追加

num_tuple = tuple(num_list)
print(num_tuple)

val = input() # 標準入力を受け付ける（ターミナルに文字を打ってから次の指示を表示できる）
num_tuple += (val,) # num_tupleに受け付けた標準入力を追加

num_set = {'40', '50', '60'}
print('num_tuple = {}'.format(num_tuple))
print('num_set = {}'.format(num_set))

print(set(num_tuple) | num_set) # タプルをセットにして和集合

num_dict = {'num_tuple' : 'num_str'} # 辞書型
print(len(num_list)) # num_listの長さ（数）

print(num_dict.get('Mykey','Does not exist')) # num_dictからMykeyを取り出す。ないときはDoes not existが表示

num_list.extend(['50', '60']) #append関数だと50で1行,60で1行になるので,50,60で1行にするにはextendを使用
print('num_list ={}'.format(num_list ))

val = input()
is_under_50 = int(val) < 50 # 標準入力が50より小さいかどうかTrueかFalse
print('is_under_50 = {}'.format(is_under_50))

print('num_str = {}'.format(num_str))
print(dir(num_dict))# num_dictが持っているメソッドを表示