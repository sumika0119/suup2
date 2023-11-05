# ファイル出力、追記


file_path = 'resources/output.csv' # output.csvというファイルを作成

f = open(file_path, mode='w', encoding='utf-8', newline='\n') # newline 改行コード
f.write('あああ\nいいい') # 書き込み(utf-8で行われる)
f.close()
with open(file_path, mode='a', encoding='utf-8', newline='\n') as f: # mode='w'は上書きされる。mode='a'は追記されう
    list_a = [                                                       #with ファイルのopenとcloseを同時に行う
        ['A', 'B', 'C'],
        ['あ', 'い', 'う']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x)) # xはlistをループさせている
    # f.writelines(list_a[0]) # listの['A', 'B', 'C']をつなげて書き込み


# open 書き込みモード（ファイルが存在しなければ作成、存在した場合は上書き）
# write ファイルに文字列を書き込み（¥nで改行）
# writelines リストをそのままつなげて書き込み
# 追記モード（ファイルが存在しなければ作成、存在した場合は追記）
