# Exception Group 複数exceptionを返す

def raise_exceptions():
    exceptions = []
    try:
        msg = 'Hello' + 0 # Type Error数字と文字列を足せない
        print(msg)
    except TypeError as e:
        e.add_note('TypeError発生しました')
        exceptions.append(e) # TypeError呼び出し元に返してしまってるので下の処理は実行されない。raiseは実行をストップする。
    try:
        num = 10 / 0 # ZeroDivisionErrror
    except ZeroDivisionError as e:
        exceptions.append(e)
    if len(exceptions) > 0:
        raise ExceptionGroup('例外発生:', exceptions)
try:
    raise_exceptions()
except *TypeError as te: # exceptグループでエラーをキャッチしたい場合、例外の前に*をつけるとよい
    print('Type Errorの場合の処理')
except *ZeroDivisionError as ze:
    print('Zero Divisionの場合の処理')
# except ExceptionGroup as eg:
#     import traceback
#     traceback.print_exception(eg)
    #print(eg)
    
# raise_exceptions()
# try:
#     raise_exceptions()
# except ZeroDivisionError as e:
#     print('Zero Div発生')
# except TypeError as e:
#     print('Type Error発生')