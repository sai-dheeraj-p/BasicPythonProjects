a3='-'*70
#addn operators
a = 2
b = 3
print('a is 2 & b is 3')
print('a+b =',a+b)
print(a3)
#subs operators
a = 2
b = 3
print('a is 2 & b is 3')
print('a-b =',a-b)
print(a3)
#multiplication operators
a = 2
b = 3
print('a is 2 & b is 3')
print('a*b =',a*b)
print(a3)
#division operators
print('5/5 =',5 / 5)
print('10/2 =',10 / 2)
print('-10/2 =',-10 / 2)
print('20.0/2',20.0 / 2)
print('5//3=',5//3)
print('20//3 =',20 // 3)
print('6%2=',6%2)
print(a3)
#exponent op
a = 2
b = 3
print('a*b =',a**b)
print(a3)
#logical op
a, b, c = True, False, True
print('a, b, c = True, False, True')
if a and c:
    print("Both a and c are True (AND condition).")
if b or c:
    print("Either b or c is True (OR condition).")
if not b:
    print("b is False (NOT condition).")
print(a3)
#and operator
a = 10
b = 10
c = -10
if a > 0 and b > 0:
    print("Numbers are greater than 0")
if a > 0 and b > 0 and c > 0:
    print("Numbers are greater than 0")
else:
    print("At least one number is not greater than 0")
#or operator
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
#not operator
a = 10
if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")