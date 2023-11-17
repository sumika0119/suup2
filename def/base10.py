# 再帰→関数から自分の関数を呼び出す

def sample(a):
    if a < 0:
        return
    else:
        print(a)
        sample(a-1)

sample(10)

# フィボナッチ
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2) # n=3だから　2+1 でなはくn=3だから fib(2)+fib(1)

for x in range(1, 10):
    print(fib(x))