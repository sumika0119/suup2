# メタクラス→クラスの定義をチェック

class MetaException(Exception): # クラスを再定義してクラスの中の値を検証したい場合に便利(例外を返す)  
    pass

class Meta1(type): # type（デフォルトのメタクラス）
    
    def __new__(metacls, name, bases, class_dict):
        print('metacls = {}'.format(metacls))
        print('name = {}'.format(name)) # メタクラスを指定したクラスが入る
        print('bases = {}'.format(bases)) # 継承しているクラスが入る（今回は入らない）
        print('class_dict = {}'.format(class_dict))
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください')
        for base in bases: # 継承しているクラス　
            if isinstance(base, Meta1): # baseがMeta1のインスタンスの場合
                raise MetaException('継承できません') # finalクラス
        return super().__new__(metacls, name, bases, class_dict) # super()で元のtypeクラスを呼び出す

class ClassA(metaclass=Meta1): # ClassAを生成した際にmetaclass=Meta1の __new__が呼ばれる
    a = '123'
    my_var = 'AAA'
    pass

class SubClassA(ClassA):# ClassAを生成した際にmetaclass=Meta1の __new__が呼ばれる。今回継承したクラスがMeta1→baseがMeta1になるので16行目がTrueになる
    pass # 継承したくないクラスを作成したいときに利用できる。このクラスはこのクラスだけで完結させたい