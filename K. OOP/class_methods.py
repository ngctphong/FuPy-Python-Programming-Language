class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def __repr__(self):
        return f'{self.first} is {self.age}'

    @classmethod
    def display_active_user(cls):
        return f'There are currently {cls.active_users} active users'

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        last = last.strip()
        age = age.strip()
        return cls(first, last, age)

    def full_name(self):
        return f'{self.first} {self.last}'

    def likes(self, thing):
        return f'{self.first} likes {thing}'

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1

    def log_out(self):
        User.active_users -= 1
        return f'{self.first} has logged out'


user1 = User('Phong', 'Nguyen', 27)
user2 = User.from_string('Tom, Jones, 65')
print(user2.first)
print(user2.last)
print(user2.age)
print(f'{user1} is totally rad')
print(user1)