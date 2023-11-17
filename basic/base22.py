# try except

try:
    b = [10,20,30]
    c = b.method_a()
    a = b[4]
    a = 10 / 0
except ZeroDivisionError as e: # エラーは発生しているがexceptでキャッチしている
    import traceback # 詳細なエラーを表示（何行目でエラーしたかなど）
    traceback.print_exc()
    # print(e, type(e)) # 発生したエラーの内容を表示させたい場合
    pass # 何も処理をしないときはpassと書く
except IndexError as e: # bには4番目の数値がないためエラーになる
    print('indexエラー発生')
except Exception as e: # 全てのエラーをキャッチ
    print('Exception:',e,type(e))
else: # 例外が発生しなかった場合実行される
    # a = 10 / 0 # elseの中でエラーが発生してもexcept ZeroDivisionErrorを書いていないのでキャッチできない
    print('Else処理')
finally: # 例外が発生してもしなくても実行される
    print('Finally処理')
print('処理が完了しました。')