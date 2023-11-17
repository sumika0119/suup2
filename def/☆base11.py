# リスト内包表記→ループと条件を使って1行でリストを作成する方法

list_a = (1,2,3,'a',4,'b') # タプル

list_b = [x*2 for x in list_a if type(x) == int] # list_aのリスト
print(list_b)
list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)


dict_a = {
    'a': 'Apple',
    'b': 'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str] #list_aが文字列の場合は(a,b)a(キー)がApple(値), ｂがBanana
print(list_c)
list_a = tuple(x for x in range(100))
print(type(list_a)) # クラス名表示
def func(n): # 特定の条件を満たす値だけ取り出すときに便利 
    for x in range(2, n):
        if n % x == 0: # ｘは1とn以外の何らかの値
            return True
        return False
    
list_a = [x for x in range(100) if func(x) == False]
print(list_a)