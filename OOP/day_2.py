# OPP
# Defining a class
class Person:
    #Attributes
    def __init__(self, name, limbs, hair_color, age):
        self.name = name
        self.limbs = limbs
        self.hair_color = hair_color
        self.age = age
        print(f'the new human {self.name} are born')
    # Methods
    def intro(self):
        print(f'Hello World from --> {self.name}')
    def ageIs(self):
        print(self.age)
    # Methods that changes things
    def birthday(self):
        # self.age = self.age +1
        self.age +=1
        print(f'Happy Birthday {self.name}, congrats on being {self.age}')


user1 = Person('Stevien', 4, 'Blond', 29)
user2 = Person('Austin', 4, "Purple", 27)

print(user1.name)

user1.name = "Steven"

print(user2.name)
user1.intro()
user2.intro()

user1.ageIs()
user1.birthday()
user1.ageIs()



