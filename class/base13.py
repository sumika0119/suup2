

# ファイル入力

file_path = 'resources/input.csv'
f =open(file_path, mode='r', encoding='utf-8') # utf-8でファイルを読み込む

line = f.read() # 中身全体を読み込む
print(line)

# lines = f.readlines() #readlines 中身を配列で読み込む
# print(lines)
# for x in lines:
#     print(x.rstrip('\n')) #改行コードを削除して読み込む

# # line = f.readline() #readline 1行ずつ読み込む
# while (line := f.readline()): #16行目19行目を1行にまとめる
#     print(line.rstrip('\n'))
#     # line = f.readline()

# f.close() # ファイルを閉じる
# # closeをしないと → メモリを食う。他の処理でファイルに開けない
# # with
# with open(file_path, mode='r', encoding='utf-8') as f: #with ファイルのopenとcloseを同時に行う #ファイルを開いて開いた結果をfに格納している
#     lines = f.readlines()
#     print(lines) #['1,2,3,\n', 'a,b,c,\n', 'A,B,c\n', 'あ,い,う']と表示される

# print(f.read()) #withの外に出ると変数は使えないのでエラーになる