# COMMENTS use hashtags
# VARIABLES
# in js we use var or let variable_name
variable_name = 9
name = 'jim'
age = 24
# DATA TYPES

# bool, string, integers, None,
# integer
# double -  2.25
# float - 3.14159
# bool - True False
# string - 'hello world'
# javascrit we had arrays myArr = [1,2,3,4,5,6,7] js we use .push .pop
# list = JS array
mylst = [1, 2, 3, 4, 5]
# for python lists we use .append() .pop
# Dictionary in python is equal to js object
name = 'jim'
my_dict = {
    'name': 'steven',
    'lname': 'Coney',
    'age': 30
}
print(my_dict)
my_dict['name'] = 'Steven'
my_dict['username'] = 's@c.com'
print(my_dict)


# STRING FORMATTING
firstName = 'Han'
lastName = 'Pak'
# console.log(firstName + lastName) javascript
fullName = f'{firstName} {lastName}'
greeting = f'Hello my name is {fullName}'
# js we use console.log() to print to the console, in python we use print()
print(greeting)
# newString = 'Hello, my name is %s %s and I am %d years old' %(fname, lname, age)
# newString = 'Hello, my name is {} {} and I am {} years old'.format(fname, lname, age)

# LOOPS
# for loops and while loops
# in JS
# for(var i=0; i<10; i++){
#     console.log(i)
# }
# range method takes 3 arguments if only one argument is given it starts at 0
# and is exclusive i<10
for i in range(10):
    print(i)

print('*'*50)

for i in range(2, 10):  # first argument is start, second argument is exclusive end
    print(i)

print('*'*50)

for i in range(30, 3, -3):  # first is the start, second is exclusive end, the third is the interval
    print(i)

# i = 0
# while i<10:
#     print(i)
#     # i = i + 1
#     i += 1

print('*'*50)

nameLst = ['Jim', 'Steven', 'John', 'Mike']
myName = 39
for i in range(0, len(nameLst)):  # in JS nameLst.length = python to len(nameLst)
    print(nameLst[i])

print('*'*50)

for name in nameLst:
    print(name)

# CONDITIONALS
# if, else, ==, <, >, !=, and, or

for i in range(10):
    if i < 5:
        print('i is less than 5')
    elif i >= 5 and i < 7:
        print(i)
    else:
        print('hurray conditionalls are almost over!!')

# FUNCTIONS set of rules / a block of code / reusable /
# function my_function(){

# }
print(" ")

# THIS IS WHERE WE DEFINE THE FUNCTION


def sayHello(name, age):
    print(f'hello {name} i am {age} years old')


# THIS IS WHERE WE CALL IT
sayHello('Darelle', 39)

# Return Statement vs print
# start my code here
name = 'jerry'
age = 98
number1 = 15
number2 = 27


def foo(num1, num2):
    # sum = num1 + num2
    print(num1+num2)
    return num1+num2


funcOut = foo(number1, number2)
print(funcOut)


# Functions basic I

# 6
def a(b, c):
    print(b+c)


print(a(1, 2) + a(2, 3))


# 11
b = 500
print(b)


def a():
    b = 300
    print(b)


print(b)
a()
print(b)

# 1 - print 500
# 2 - print 500
# 3 - print 300
# 4 - print 500
