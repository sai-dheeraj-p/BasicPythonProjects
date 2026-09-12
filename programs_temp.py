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
