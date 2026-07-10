a1="-"*80
s={'one',2,3,4,'five'}
print(s)
print(a1)

a=[1,2,3,4,5,6]
print("a :",a)
s=set(a)
print("set s :",s)
print(a1)

set_a1={11,22,33,44}
print("given set :",set_a1)
print("iterating through the set :")
for ab in set_a1:
    print(ab)
print(a1)

seta={1,2,3,4,5,6}
print("given set :",seta)
seta.add(7) #add()
print("new set with added element \'7\' :",seta)
seta.update([8,9,10]) #update()
print("new set with updated mult. element :",seta)
print(a1)

set1={1,2,3,4,5,6}
print("given set :",set1)
set1.remove(6) #remove()
print("updated set (removed 6) :",set1)
set1.discard(5) #discard()
print("updated set (discarded 5) :",set1)
set1.pop() #pop()
print("updated set (popped a random element) :",set1)
set1.clear() #clear()
print("removed all elements from the set :",set1)
print(a1)

setA = {1,2,3}
print("Set A:", setA)
setB = {2,3,4,5}
print("Set B:", setB)
print("Union of Sets A and B:")
print("Method 1(setA|setB)):", setA | setB) #'|'
print("Method 2(setA.union(setB)):", setA.union(setB))  #union()
print(a1)

setA = {1,2,3,4}
print("Set A:", setA)
setB = {2,3,4,5}
print("Set B:", setB)
print("Intersection of Sets A and B:")
print("Method 1(setA & setB):", setA & setB)  #'&'
print("Method 2(setA.intersection(setB)):", setA.intersection(setB))  #intersection()
print(a1)

setA = {1,2,3}
print("Set A:", setA)
setB = {2,3,4,5}
print("Set B:", setB)
print("A - B:")
print("Method 1(setA - setB):", setA - setB)  #'-'
print("Method 2(setA.difference(setB)):", setA.difference(setB))  #difference()
print("B - A:")
print("Method 1(setB - setA):", setB - setA)  #'-'
print("Method 2(setB.difference(setA))):", setB.difference(setA))  #difference()
print(a1)