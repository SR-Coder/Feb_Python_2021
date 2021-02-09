def twoTimes(num):
    return num*2

timestwo = lambda n,m: n*m
x = 5
y = 6
timestwo(x,y)


def square(num):
    return num**2
mylist = [1,2,3,4,5,6]

print(mylist)
squared = map(lambda num: str(num), mylist)
newLst = []
for x in squared:
    newLst.append(x)
print(newLst)