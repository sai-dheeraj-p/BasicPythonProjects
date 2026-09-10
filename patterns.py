a1='-'*90
#square pattern
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        print('*', end=" ")
    print()
print(a1)
#triangle pattern
n=int(input("enter a number :"))
for i in range(n):
    for j in range(i+1):
        print('*', end=" ")
    print()
print(a1)
#descending triangle
n=int(input("enter a number :"))
for i in range(n):
    for j in range(n-i):
        print('*', end=" ")
    print()
print(a1)
#pyramid pattern
n=int(input("enter a number :"))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end=" ")
    for k in range(i*2+1):
        print('*', end=" ")
    print()
