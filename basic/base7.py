fruit = 'apple'
print(fruit)
print(type(fruit))
print(fruit * 10)
fruit_10 = fruit * 10
print(fruit_10)

new_fruit = fruit + ' banana'
print(new_fruit)

fruits = """apple
banana
grape
"""
print(fruits)

fruit = 'banana'
print(fruit[-1])

byte_fruit = fruit.encode('utf-8')
print(byte_fruit)
print(type(byte_fruit))

str_fruit = byte_fruit.decode('utf-8')
print(str_fruit)
print(type(str_fruit))


msg = 'ABCDEABC'
print(msg.count('ABC'))

print(msg.startswith('ABECD'))
print(msg.endswith('C'))

msg = ' ABC '
print(msg)
print(msg.strip())
msg = 'ABCDEFABC'
print(msg.strip('CBA'))
print(msg.lstrip('CBA'))
print(msg.rstrip('CBA'))

msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u,msg_l,msg_s)

msg = 'ABCDEABC'
msg_r = msg.replace('ABC','FFF',1)
print(msg_r)

msg = 'hello World'
print(msg.capitalize())


msg = 'hello, my name is taro'
print(msg[1:10:2])
print('hello {}'.format('Taro'))
name = 'Jiro'
print(f'hello {name}') #3.6以上
print(f'{name=}') #3.8以上

msg = 'apple'
print(msg.islower()) #小文字か
print(msg.isupper()) #大文字か

msg = 'ABCDEABC'
print(msg.find('ABC')) #文字列のインデックスを検索〈最初に出てくる〉インデックスが表示
print(msg.rfind('ABC'))# 文字列のインデックスを右端から検索〈左から数えてインデックスは５）
print(msg.index('ABC')) 
print(msg.rindex('ABC'))

print(msg.find('ABCE')) #見つからない場合-1で出表示
print(msg.rindex('ABCE'))#見つからない場合エラー


