a='-'*70
A=[1,'two','THREE',4.5,[5,'six','SEVEN']]
print(A)
print(a)

list_1=[23,45,86.4,86.4,88,43,'zero']
list_1[0]='twenty three'
print(list_1)
print(a)

print(list_1[-1])
print(list_1[2])
print(a)

empty_list=[]
print(empty_list)
print(a)

list_2= [11, 22.3, 'thirty three', 'forty four']
list_2.insert(2,22.9)
list_2.extend([55,66,77,88.8])
print(list_2)
print(a)

list_3=[1,2,3,3,4.4,'five',5.1,5.5,6,7]
list_3.remove(3)
list_3.pop(-1)
print('popped element:',list_3.pop(-1))
del list_3[-2]
print(list_3)
print(a)

list_4=[1,2,3,4]
print('length of list_4 :',len(list_4))
print(a)

list_5=[1,2,3]
print('iterating list using for loop :')
for x in list_5:
    print(x)
print(a)

list_6=[8390,382,489,548,230234,48387,13,999]
print('given list to sort :',list_6)
list_6.reverse()
print('reversed list :',list_6)
list_6.sort()
print('sorted list :',list_6)
print(a)

list_7=[99,36,72,44,62,81,11]
print('given list :',list_7)
print('largest number:',max(list_7))
print('smallest number:',min(list_7))
