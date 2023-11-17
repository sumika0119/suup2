# with 

class WithTest:

    def __init__(self, file_name):
        print('init called')
        self._file_name = file_name

    def __enter__(self):
        print('enter called')
        self.__file = open(self._file_name, mode='w', encoding='utf-8') #（WithTesutの引数のHelloが表示される）
        return self
    
    def write(self, msg):
        self.__file.write(msg)
    
    def __exit__(self, exc_type, exc_val, traceback): # エラーが発生したときのエラーハンドリングのためにある引数。exitを定義するためには引数が3つ必要（何でも良い）
        print('exit called')
        self.__file.close()

with WithTest('resources/output.txt') as t: # output.txtが作成され、その中にああああと入力される
    print('with の中') # withから外に出るとき__exit__が呼ばれる
    t.write('ああああ')
