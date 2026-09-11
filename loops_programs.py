a1='-'*90
#count digits problem
n=int(input("enter a number :"))
x=0
while n>0:
    n=n//10
    x+=1
print("the no. of digits in the number are :",x)
print(a1)
#factorial
fact=1
n=int(input("enter a number :"))
for i in range(2,n+1):
    fact=fact*i
print("the no. of ways the number can be arranged is (factorial) :",fact)
print(a1)
#gcd
n=int(input("enter number 1 :"))
m=int(input("enter number 2 :"))
small = min(n , m)
gcd=1
for i in range(1,small+1):
    if n % i == 0 and m % i == 0:
        gcd=i
print(gcd)
print(a1)
#lcm
n=int(input("enter a number :"))
m=int(input("enter number 2 :"))
lcm=1
for i in range(max(n,m),n*m+1):
    if i % n == 0 and i % m == 0:
        lcm=i
        break
print("lcm is (using for):",lcm)
#lcm using while
n=int(input("enter a number :"))
m=int(input("enter number 2 :"))
lcm=1
while lcm<n*m:
    if lcm % n == 0 and lcm % m == 0:
        break
    lcm+=1
print("lcm is (using while)",lcm)
print(a1)
#fibonacci
n=int(input("enter a number :"))
if n==0:
    print(0)
elif n==1:
    print(1,1)
else:
    print(1,1,end=" ")
    a=1
    b=1
    for i in range(2,n+1):
        fibo=a+b
        a=b
        b=fibo
        print(fibo,end=" ")
print(a1)
#prime no's
n=int(input("enter a number :"))
if n<=1:
    print("the given number is not a prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            print("the given number is not a prime number")
            break
    else:
        print("the given number is  a prime number")
print(a1)
#all divisors of a no.
n=int(input("enter a number :"))
for i in range(1,n+1):
    if n%i == 0:
        print(i,end=" ")
print(a1)
#optimizing the above prog
n = int(input("enter a number :"))
x = 1
l=[]
print("the factors are :")
while x * x < n:
    if n % x == 0:
        l.append(x)
        l.append(n//x)
    x += 1
if x * x == n:
    l.append(x)
l.sort()
print(l)
