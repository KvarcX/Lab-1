#ЦЕЙГАЛОВ АНДРЕЙ ВЛАДИМИРОВИЧ БИН2202
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if d < 0:
    print("корней нема")
    exit()
x1 = (-b+d**0.5)/(2*a)
x2 = (-b-d**0.5)/(2*a)
if x1!=x2:
    print(x1,x2)
else:
    print(x1)