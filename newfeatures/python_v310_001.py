
def check_size(size: str):
    match size:
        case 'L' | 'XL': # LとXL
            # print('Lサイズです')
            print('大きめのサイズ')
        case 'M':
            print('Mサイズです')
        case 'S':
            print('Sサイズです')
        case _:
            print('このサイズは存在しません')

    print('サイズチェック完了しました')

# check_size('L')
# check_size('P') # 選択肢にPはないので、＿（11行目）が呼ばれる
# check_size('XL')

# ガード
def check_size_price(size: str, price: int):
    match size:
        case 'L' if all([price > 0, price < 2000]):
            return 'Lサイズです' # returnが実行されると関数の中のその後の処理が全部実行されない
        case 'M' if price > 0:
            return 'Mサイズです'
        case _:
            return 'サイズと価格の指定が誤っています'
        
print(check_size_price('L',1999))
print(check_size_price('M',100))
print(check_size_price('M',-200))