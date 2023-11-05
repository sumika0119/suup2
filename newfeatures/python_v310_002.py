# type hinting(型の指定をつける)
def add_number(a: int | float, b: int | float) -> int |float :
    return a + b

additional_number = add_number(12.2,21)

def print_msg(msg: str):
    print(msg)

# print_msg(additional_number)

number = 12

print(isinstance(number, int))
print(isinstance(additional_number, int | float |complex | str)) #int, float, complex, strのどれかだったらTrue