from typing import Self

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def compare(self: Self, other: Self) -> bool: # 1つ目の引数にはuser1,　2つ目の引数にはuser2が入って比較してる
        return self.name == other.name and self.age ==other.age
    
    def copy(self: Self) -> Self:
        return User(self.name, self.age)


user1 = User('Taro', 18)
user2 = User('Taro', 18)
msg = 'Hello'

print(user1.compare(user2)) # otherにmsgが入っているがmsgは.name、.ageが存在しないのでエラーになる
# print(user1.compare(msg))
user3 = user1.copy()
print(user1.compare(user3))