#if-else_program_1
n=int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
#program_2
n=int(input("Enter a number: "))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")
#program_3
n=int(input("Enter a number: "))
if n>0 and n%2 == 0:
    print("positive and even")
elif n>0 and n%2 != 0:
    print("positive and odd")
elif n<0 and n%2 == 0:
    print("negative and even")
elif n<0 and n%2 != 0:
    print("negative and odd")
else:
    print("zero")
#program_3_other method
n=int(input("Enter a number: "))
if n>0:
    print("positive",end=" ")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
elif n<0:
    print("negative",end=" ")
    if n%2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("zero")
#program_4
a=int(input("Enter the 1st number (a): "))
b=int(input("Enter the 2nd number (b): "))
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a and b are equal")
#program_5
a=int(input("Enter the 1st number (a): "))
b=int(input("Enter the 2nd number (b): "))
c=int(input("Enter the 3rd number (c): "))
if a>b and a>c:
    print("a is the greatest")
elif b>c:
    print("b is the greatest")
else:
    print("c is the greatest")
#program_5
n=int(input("Enter a year: "))
if n%4==0 and (n%100!=0 or n%400==0):
    print("the given year is a leap year")
else:
    print("the given year is not a leap year")
#program_6
print('''available operation are :
       1.add  
       2.subtract  
       3.multiply  ''')
n=int(input("please select an operation 1 , 2 or 3 : "))
if n==1:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("the sum is ",a+b)
elif n==2:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("the difference is ",a-b)
elif n==3:
    a=int(input("enter the first number: "))
    b=int(input("enter the second number: "))
    print("the product is ",a*b)
else:
    print("invalid operation")