# セット

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}


u = s | t # 和集合
# u = s.union(t) # 和集合

print(u)

u = s & t # s.intersection(t) 積集合
print(u)

u = s - t # s.difference(t) 差集合
print(u)

u = s ^ t # s.symmetric_difference(t)対象差
print(u)

s |= t
print(s)

# issubset issuperset isdisjoint
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}
u = {'cherry'}

print(s.issubset(t)) # ｓがｔの集合のサブになっているか（ｔの中にsが含まれているか）
print(s.issuperset(t)) # ｓがｔのスーパーになっているか（ｓの中にｔが含まれているか）
print(s.isdisjoint(u)) # ｓとｔの重なっている要素がないか 