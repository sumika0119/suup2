# removeprefix(接頭語の指定文字を削除), removescffix（接尾語の削除）
msg = ' Hello World, Hello'

msg2 = msg.removeprefix("He")

msg3 = msg.replace("He", "") # 文章の中の文字が変換
print(msg2)
# lo World, Hello
print(msg3)
# llo World, llo（Heを削除）スペースが１つでもあると削除されない

# 接尾語の削除
msg = 'Hello World'
print(msg.removesuffix('World'))