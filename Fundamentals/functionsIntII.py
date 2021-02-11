x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# 1. change the value 10 in x to 15

def functionOne(lst, idx, cngVal):
    print(lst)
    print[idx[0], idx[1]]
    lst[idx[0]][idx[1]] = cngVal
    # lst[1][0] = cngVal
    print(lst)
    return lst

# functionOne(x,[3,0],15 )

# 2 Change the last_name of the first student from 'Jordan' to 'Bryant'
def functionTwo(lst, lstName):
    print(lst)
    lst[0]['last_name'] = lstName
    print(lst)


functionTwo(students, 'Myers')

# 3 In the sports_directory, change 'Messi' to 'Andres'
def functionThree(my_dict, keyName, idx, val):
    print('*'*50)
    print(my_dict)
    my_dict[keyName][idx]=val
    print(my_dict)

functionThree(sports_directory, 'basketball', 2, 'Scott')

# 4 Change the value 20 in z to 30
def functionFour(lst, idx, mykey, myval):
    print(lst)
    lst[idx][mykey] = myval
    print(lst)

functionFour(z, 0,'y', 30)