# if and or not

# msg = 'yellow'
# if msg == 'blue' : # mas = blueの場合
#     print('すすめ') 
# elif msg == 'red' : # msg = red の場合（ifで設定したもの以外）
#     print('止まれ')
# else:
#     print('それ以外の処理')

age = 60
if age < 20:
    print('20未満')
elif age <= 40: # 20以上で実行される
    print('20以上40以下です') 
elif age >= 60:
    print('60以上です')
else:
    print('それ以外の年齢')

# and or not

gender = 'woman'
age = 30
if gender == 'man' or age < 20: #　and どちらも満たしていると表示 # or どちらか満たしていれば表示 #満たさないとき何も出ない
    print('未成年男性です')

if not gender =='man':
    print('男性ではない')
