#  演習４
class CharacterAlreadyExistException(Exception): # 同じ名前の時は例外を返す処理を規定。(クラス名)をすると自分で例外を否定することができるようになる
    pass

class AllCharacters: # クラスの中にクラス変数が3つ存在する

    all_characters = [] # 現在存在する全てのキャラクター
    alive_characters = [] #生きているキャラクターを格納するクラス
    dead_characters = [] # 死んだキャラクターを全て格納する

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:# 既にall_characters似名前が存在する場合
            raise CharacterAlreadyExistException('キャラクターはすでに存在しています') #例外処理はraise
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls, name): # キャラクターを削除するクラスメソッドを作成
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:

    def __init__(self, name, hp, offense, defense): # コンストラクタ（インスタンスを作成するときに呼び出す）
        AllCharacters.character_append(name) #Allcharactersクラスにキャラクターを追加
        self.name = name # インスタンス変数を初期化（違うクラスに前のクラスで設定したname, ho, offencu, defenceを引き継がれないようにするため）
        self.hit = help
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print('キャラクターはすでに死んでいます')
            return # return　関数内での処理は終了し呼び出し元に処理が返る
        attack_point = self.offense - enemy.defense
        attck_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name) #クラス名.メソッド名（defの後の変数）でAllCharactersクラスの中にあるcharacter_deleteを呼び出す
            # 20,21行目にenemyのnameが追加される
             
    def critical_hit(self, enemy):
        self.attack(enemy, 2)

character_a = Character('A', 10, 5, 3)
character_b = Character('B', 8, 6, 2)

print(character_b.hp)
character_a.critical_hit(character_b) # 8→2
print(character_b.hp)
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
character_a.attack(character_b) # 2→1
print(AllCharacters.alive_characters)
print(AllCharacters.dead_characters)
character_b.attack(character_a)
character_c = Character('A', 20, 5, 3) # 同じ名前があると例外処理が返ってくる