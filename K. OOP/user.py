class User:
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

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
print(user1.first)
print(user1.last)
print(user1.age)
print(user1.full_name())
print(user1.likes('Lemon'))
print(user1.is_senior())
print(user1.birthday())
print(user1.age)
print(User.active_users)


class Person:
    def __init__(self):
        self.name = 'Phong'
        self._secret = 'private'
        self.__msg = 'I like apples'


p = Person()
print(p._secret)
print(p._Person__msg)


class Moderator(User):
    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community

    def remove_post(self):
        return f'{self.full_name()} removed a post from the {self.community} community'


jasmin = Moderator('Jasmine', "0'corner", 61, 'Piano')
print(jasmin.full_name())
print(jasmin.community)