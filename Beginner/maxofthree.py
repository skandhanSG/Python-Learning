a=input("enter 1")
b=input("enter 2")
c=input("enter 3")
print(max(a,b,c))
if (a>b and a>c):
    print(a)
elif(c>b and c>a):
    print(c)
else:
    print(b)
    