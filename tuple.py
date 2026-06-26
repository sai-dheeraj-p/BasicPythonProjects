from pip._internal.commands import index

a='-'*70
A=(1,'two','THREE',4.5,(5,'six','SEVEN'))
print()
print(A)
print(a)

tuple_1=(23,45,86.4,86.4,88,43,'zero')
print(tuple_1)
print(tuple_1[3])
print(tuple_1[-1])
print(a)

empty_tuple=()
print('empty tuple :',empty_tuple)
mixed_tuple=(1,2,'three',(4,5,6),{7,8,9})
print('mixed tuple :',mixed_tuple)
print(a)

tuple_2=(11,22,33,44,55,66,77,888,99)
print('tuple :',tuple_2)
print('elements between indices 1 and 7 :',tuple_2[1:9])
print('elements between indices 0 and -5 :',tuple_2[:-5])
print(a)

#tuple concatenation
tuple_3=(1,2,3)
print('tuple :',tuple_3+(4,5,6))
print(a)

#changing/adding elements : tuple to list to tuple
tuple_4=(1,2,3,4,5,6)
print('tuple before :',tuple_4)
list_1=list(tuple_4)
list_1.extend([7,8,9])
tuple_4=tuple(list_1)
print('tuple after :',tuple_4)
print(a)

#tuple unpacking
tuple_5=(11,22,33,44,55,66)
print('given tuple :',tuple_5)
(v1,v2,v3,v4,v5,v6)=tuple_5
print('first element of tuple :',v1)
print('second element of tuple :',v2)
print('third element of tuple :',v3)
print('fourth element of tuple :',v4)
print('fifth element of tuple :',v5)
print('sixth element of tuple :',v6)
print(a)

#tuple operations
tuple_a=(2,4,5)+(6,8,9)
print('tuple concat :',tuple_a) #concatenation

tuple_b= ('banana',)*3
print('tuple repetition :',tuple_b) #repetition

tuple_c= (13,43,7656,24,987,66)
print('tuple :',tuple_c)
print('is 43 present in tuple :',43 in tuple_c)
print('is 55 present in tuple :',55 in tuple_c)
print(a)

#tuple methods
tuple_a=(1,2,3,3,3,4,5,6)  #count()
print('original tuple :',tuple_a)
print('occurrence of \'3\' in tuple_a :',tuple_a.count(3))
print(a)

tuple_b=(1,2,3,3,3,4,5,6)  #index()
r1=tuple_b.index(3)
r2=tuple_b.index(6,3)
r3=tuple_b.index(4,3,7)
print('first occurrence of \'3\' in tuple_b :',r1)
print('first occurrence of \'6\' after 3rd index in tuple_b :',r2)
print('first occurrence of \'4\' after 3rd index and before 7th index in tuple_b :',r3)
print(a)

tuple_a=(1,2,3,3,3,4,5,6) #max()
print('original tuple :',tuple_a)
largest_element=max(tuple_a)
print('largest element of tuple :',largest_element)
print(a)

tuple_a=(1,2,3,3,3,4,5,6) #min()
print('original tuple :',tuple_a)
smallest_element=min(tuple_a)
print('smallest element of tuple :',smallest_element)
print(a)

tuple_a=(1,2,3,3,4,5,7,6) #len()
print('original tuple :',tuple_a)
print('length of the tuple :',len(tuple_a))
print(a)