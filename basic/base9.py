list_a = [1,2,3,4]
list_b = []

print(list_a)
print(list_a[-2])

list_a = [1,[1,2,'apple'],3,'banana']
print(list_a)
list_a[1][2] = 'lemon'
print(list_a)
#リストメソッド
list_a = [1,2,3,4,5]

list_b = list_a[:3]#２まで
print(list_b)
list_b = list_a[3:]#３から
print(list_b)
list_b = list_a[1:4:2]#１から３まで１つとばし
print(list_b)

#append,extend,insert,clear

list_a.append('apple')#リストの追加
print(list_a)
list_a.append(['banana', 'melon'])
print(list_a)

list_a.extend(['banana', 'melon'])#リストの拡張〈横につなげる〉
print(list_a)
list_a.insert(1, 'grape')#特定の場所〈インデックスの１番目〉に要素を追加
print(list_a)
# list_a.clear()#リストを空にする
# print(list_a)

#remove,pop,count,index
list_a = [0,1,1,2,2,3,3,3,4]
list_a.remove(3) #1番最初に出てくる３を削除
print(list_a)
value = list_a.pop()#1番最後に追加された要素(value = 4)を取り出す
print(list_a,value) 
print(list_a.count(1))#１が何個あるか表示
print(list_a.index(2))#２が1番最初に登場するインデックスを表示

# copy
# print(list_a)
# list_b = list_a
# list_b[0] = 'AAAAA'
# print(list_a) #list_bを変えたつもりがlist_aも書き換わる〈格納している場所が一緒だから〉

list_b = list_a.copy()#copyを使うとlist_aの中身の値を新たに作成して別の場所に格納してくれる→値が書き換わらない
list_b[0] = 'AAAAA'
print(list_a)

# sort,reverse
list_a = ['banana', 'apple', 'lemon', 'grape']

print(list_a)
# list_a.sort() #要素の昇順並び替え
list_a = sorted(list_a)
list_a.reverse()
print(list_a)#要素の逆順並び替え〈今は昇順なので降順に並べ変わる〉
