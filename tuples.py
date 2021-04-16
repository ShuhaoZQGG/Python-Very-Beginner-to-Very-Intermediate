
mytuple = ("Max", 28, "Boston")
print(mytuple)
print(type(mytuple))

mytuple2 = ("Max") ## , is needed before the closing paranthese if only one string
print(mytuple2)
print(type(mytuple2))

mt3 = tuple(["Max", 28, "Boston"])                                      ## mt indicates mytuple + number
print(mt3)
print(type(mt3))

item = mytuple [0]
print(item)

item2 = mytuple [-2]
print(item2)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print("No")

mt4 = ('a', 'b', 'c' ,'d')
print(mt4.count('c'))
print(mt4.count('z'))
print(mt4.index('c'))

## convert tuple to list and vice versa

mylist = list(mytuple)
print(mylist)

mt5=tuple(mylist)
print(mt5)

a = (1,2,3,4,5,6,7,8,9)
b =  a[::-1]
print(a)
print(b)

mt6 = "Max", 28, "Boston"
name, age, city = mt6
print(name)
print(age)
print(city)

mt7 = ("Max", 180, 90, 35, "Boston")
name2, *data, city2 = mt7
print(name2)
print(*data) ## height, weight, age
print(city2)

## tuple is more efficient when working with large data