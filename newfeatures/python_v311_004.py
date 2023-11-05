from typing import LiteralString #(tpe hintingだがinputの形で実行時に動的に変わるような文字列を受け付けないタイプ)

def print_msg(msg: LiteralString):
    print(msg)


# val = input() # valに値が入る
val = 'Hello' # 実行後にvalの値が書き換わったりしないから○　# inputのように書き換わる物は×（ユーザーに間違った入力をしてほしくないときに使う）
print_msg(val)

def get_request(self, request: LiteralString):
    print_msg(request)