"""
class definitions
attribute is what object has
method is what object do. when function is attached to object it is called method
"""


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_01 = User("001", "Farhaan")
user_02 = User("002", "Rakesh")

user_01.follow(user_02)
print(user_01.follower)
print(user_01.following)
print(user_02.follower)
print(user_02.following)
