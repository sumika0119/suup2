# type checking

def add(a: int, b: int):
    return a + b

def print_msg(msg:str):
    print(msg.upper())

print_msg('hello') # HELLO
# print_msg(21)

# List
def print_fruits(fruits: list[str]):
    for fruit in fruits:
        print(fruit)

print_fruits(['apple', 'grape'])

# class
class ClassA:
    pass
class_a = ClassA()

def func_a(class_a:ClassA):
    pass

func_a(class_a)