a1=('-'*80)
#range
r=range(10,20)
l=list(r)
print(l)

r=range(10,20,2)
l=list(r)
print(l)

r=range(20,10,-2)
l=list(r)
print(l)

#for loop
l=[1,2,3,4,5]
for i in l:
    print(i)
print(a1)

for x in range(5):
    print(x)
print(a1)

for x in range(20):
    if x%5==0:
        print(x)
print(a1)

l=[1,2,3,4,5]
for i in range(len(l)):
    print(i , l[i])
print(a1)

#tables using for
x=int(input("enter the number :"))
for i in range(1,11):
    print(x*i)

x=int(input("enter the number :"))
y=int(input("enter the number of multiples :"))
for i in range(1,y+1):
    print(x*i)


#while loop
n=int(input("enter the number :"))
i=0
while i<n:
    print("drj")
    i=i+1
print(a1)

#tables using while
n=int(input("enter the number :"))
i=1
while i<=10:
    print(n*i)
    i=i+1
print(a1)

n=int(input("enter the number :"))
m=int(input("enter the number of multiples :"))
i=1
while i<=m:
    print(n*i)
    i=i+1
print(a1)

#break
n=int(input("enter the number :"))
for i in range(2,n+1):
    if n%i==0:
        print(i)
        break
print(a1)

n=int(input("enter the number :"))
x=2
while x<=n:
    if n%x==0:
        print(x)
        break
    x=x+1
print(a1)

#continue
n=int(input("enter the number :"))
for i in range(1,n+1):
    if i%5==0:
        continue
    print(i)
print(a1)

n=int(input("enter the number :"))
while i < n:
    if i%5==0:
        i=i+1
        continue
    print(i)
    i=i+1
print(a1)

#nested loops
#print tables from 1 to 10
for i in range(1,11):
    print(i, end=": ")

    for n in range(1,11):
        print(n*i,end=" ")
    print()
print(a1)

#traversing through a list with lists
ll=[[1,2,3],[4,5,6],[7,8,9]]
for i in ll:
    for j in i:
        print(j,end=" ")
    print()
print(a1)