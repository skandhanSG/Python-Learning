value=int(input("Enter the series n: "))

a=0
b=1
num=["0"]
#print (" 0")
for i in range(value):
    c=a
    a=b
    b=c+a
    num.append(b)
    print(num)

