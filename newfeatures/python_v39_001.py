## dictの連結

# dictの作成
ages = {
    'Taro':21,
    'Jiro':31
}

ages_2 = {
    'Saburo':18,
    'Hanako':21,
    'Taro':35
}

# update連結処理(python<=3.8)
ages_3 = {**ages, **ages_2} # 連結されると後で書いた値をベースを更新される
print(ages_3)

def name_age(name, age):
    print(f'name = {name}')
    print(f'name = {age}')

man = {
    'name':'Taro',
    'age':23
}
name_age(**man) # name_age(name, age)は引数2つだからここも引数１つでは呼び出せない。→**とつけることで内部的にmanが展開されて実行できる

# python3.9での連結方法({**dict1, **dict2} => dict1 | dict2)
ages_4 = ages | ages_2

print(ages_4)
