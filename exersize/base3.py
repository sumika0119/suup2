# 勝った場合はループの外、負けた場合３回でループの外、あいこはあいこと表示

def generate_enemy_hand(): # generate関数はyieldを用いる
    while True: #一般的なループ処理では、for文を使うことが多いが無限ループなど特殊なときはwhile文を用いた方がよい
        yield '1'
        yield '2'
        yield '3'

def is_win(my_hand, enemy_hand):
    if my_hand == '1' and enemy_hand == '2':
        return True
    elif my_hand == '2' and enemy_hand == '3':
        return True
    elif my_hand == '3' and enemy_hand == '1':
        return True
    else:
        return False
    
hands_dict = {
    '1': 'グー', # 見やすくするため改行
    '2': 'チョキ',
    '3': 'パー'
}

from random import randint # 出し手をランダムに

lose_count = 0
enemy_hands = generate_enemy_hand()

while True:
    my_hand = input('何を出しますか? 1:グー, 2:チョキ, 3:パー')
    if my_hand not in ('1', '2', '3'):
        print('間違った入力です')
        continue
    #enemy_hand = next(enemy_hands) # next→yieldの値を順番に取ってくる # 処理を実行するための関数next
    enemy_hand = str(randint(1, 3)) # randent→1-3の値がランダムに出る
    print('あなたの出した手は:{},相手の出した手は:{}'.format(hands_dict.get(my_hand),hands_dict.get(enemy_hand)))
    if my_hand == enemy_hand:
        print('あいこ')
    elif is_win(my_hand, enemy_hand):
        print('あなたは勝ちました')
        break # ループから抜け出す
    else:
        lose_count += 1
        if lose_count == 3:
            print('あなたは負けました')
            break # ループから抜け出す
        else:
            print('あなたは負けました。再チャレンジ')