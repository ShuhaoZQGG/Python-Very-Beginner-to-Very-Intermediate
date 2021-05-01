#two available syntax for dictionary
#name, age, city are the keys, Max, 28 and New York are values
mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name ="Marry", age = 28, city= "New York")
print(mydict2)

value = mydict["name"]           #choose value of the key
print(value)

value2 = mydict["city"]
print(value2)

mydict["email"]="marry@xyz.com"   #add key and value
print(mydict)

mydict["email"]="max@xyz.com"      #change key and value
print(mydict)



#remove any key and value
del mydict["name"]
print(mydict)

#femove the last pair of key and value
mydict.popitem()
print(mydict)

if "age" in mydict:
    print(mydict["age"])

try:
    print(mydict["lastname"])
except:
    print("Error: cannot find")

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

## copy is pointed to the original one, similar to list
mydict_cpy = mydict
mydict_cpy["name"] = "Max"
print(mydict)
print(mydict_cpy)

mydict_cpy = dict(mydict) # or mydict.copy()
mydict_cpy["email"]="max@xyz.com"
print(mydict)
print(mydict_cpy)

mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict2 = dict(name ="Marry", email="marry@xyz.com", city= "Boston")


print(mydict)

mydict = {3:9, 6:36, 9:81}
print(mydict)

value = mydict[3]
print(value)

## tuple can be key in dict, but not for list!
mytuple = (8,7)
mydict2 = {mytuple:15}
mydict.update(mydict2)
print(mydict)