mylist = [1,2,3,4,5,6]
a = mylist[::2]
print(a)
b = [i*i for i in mylist]

print(mylist)
print(b)

list_org=["banana","cherry","apple"]

list_cpy=list_org
list_cpy.append("lemmon")

list_cpy2 = list_org.copy() ## list_copy = list_org [:]
list_cpy2.append ("grape")

print(list_org)
print(list_cpy)
print(list_cpy2)