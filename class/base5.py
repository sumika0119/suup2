# 特殊メソッド

class Human:

    def __init__(self, name, age, phone_number): # 3つのインスタンスメソッドを持ったコンストラクタを定義
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self): # 特殊メソッド
        return self.name + ',' + str(self.age) + ',' + self.phone_number
    
    def __eq__(self, other): # ==を実行する際に呼ばれる
        return (self.name == other.name) and (self.phone_number == other.phone_number) # 名前と番号が合っていればTrueにしたいとき。# 2行目からselfにmanが入ってotherにman2が入る
        
    def __hash__(self):
        return hash(self.name + self.phone_number) # hash関数→文字列をある数値に変換する(25-27行目)辞書型でキーに値を入れ得るとき、セット型（重複を許さない配列）に値を入れるときに使う

    def __bool__(self): # ifで呼ばれる。どんなときにTrueでどんなときにFalseか
        return True if self.age >= 20 else False
    
    def __len__(self):
        return len(self.name) # nameの値の数を返す（Taroの文字数は4）
            
man = Human('Taro', 20, '08011111111')
man2 = Human('Taro', 18, '08011111111')
man3 = Human('Jiro', 18, '09011111111') # これをセットに入れたい場合はhashが定義されていないといけない
man_str = str(man)
print(man_str) # 10行目が呼ばれる # 別の文字列型に分かりやすい形で型変換するとき、__strメソッドが呼ばれる

print(man == man2)
print(hash('Taro'))
print(hash('Taro'))
print(hash('Jiro'))
set_men = {man, man2, man3}# セットは重複を許さないので同じ文字列の物は1つになってしまう※
for x in set_men:
    print(x) # 14行目でname and phone_numberにしているので両方が同じman, man2はどちらかしか入らない
if man: # if文で条件判定している場合は内部的には19行目のboolが呼ばれる
    print('manはTrue')
if man2:
    print('man2はTrue')

print(len(man)) #内部的には22行目のlenが呼ばれる
print(len(man2))