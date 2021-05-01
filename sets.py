#Sets: unordered, mutable, no duplicates

myset = set("Hello")
print(myset)

myset = {}
print(myset)

myset = set()
print(myset)

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.pop()
print(myset.pop()) ##return arbitrary element, also remove this element and update the set
print(myset)

myset.remove(3)
print(myset) ## if the remove element is not in the set, raise an error message

myset.discard(5) ## No error message
print(myset)


myset.clear()
print(myset)


print(myset)

myset = {1,2,3}
for i in myset:
    print(i)

if 1 in myset:
    print("yes")

## Unions and Intersections
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

## Union combines both sets without duplication --- Like 'OR'
u = odds.union(evens) 
print(u)

## Intersection outputs the common element in both sets --- Like 'AND'
inter = odds.intersection(evens)
print(inter)

inter = odds.intersection(primes)
print(inter)

inter = evens.intersection(primes)
print(inter)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# different elements in A between A and B
diff = setA.difference(setB)
print(diff)

# different elements in B between A and B
diff = setB.difference(setA)
print(diff)

# all different elements between A and B
diff = setB.symmetric_difference(setA)
print(diff)

# updating A without duplication
setA.update(setB)
print(setA)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# updating A by removing the different elements between A and B
setA.difference_update(setB)
print(setA)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

# combining and removing the common elements
setA.symmetric_difference_update(setB)
print(setA)

#subset means all the elements from 1st set are also in 2nd set
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3}
print(setA.issubset(setB))
print(setB.issubset(setA))

#superset means all the elements from 1st set contain all the elments in 2nd set
print(setA.issuperset(setB))
print(setB.issuperset(setA))

#disjoint: Not a element in set A is in set B
setC={7,8}
print(setA.isdisjoint(setB))
print(setB.isdisjoint(setC))

setB=setA.copy()
setB.add(10)
print(setA)

#copy issue, similar to list, tuples...
setB=set(setA)
setB.add(10)
print(setA)

setB = setA
print(setB)
setB.add(10)
print(setA)

#with frozenset, all attempts to midify the set will cause an error
a = frozenset([1,2,3,4])
print(a)