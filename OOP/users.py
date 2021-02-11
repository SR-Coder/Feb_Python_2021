class User:
    def __init__(self, userName = 'none', userAge = 0):
        self.name = userName
        self.age = userAge
    #METHODS AFTER THIS
    def changeName(self, newName):
        self.name = newName
        return self
    def birthday(self):
        self.age+=1
        return self

user1 = User()
user2 = User(userAge=92, userName='pear')
print(user1.name, user1.age, user2.name, user2.age)

user1.changeName('Jonny5')
user1.age = 39
print('*'*50)
print(user1)
print(user1.changeName('Steve').birthday())
print('*'*50)
print(user1.name, user1.age, user2.name, user2.age)

