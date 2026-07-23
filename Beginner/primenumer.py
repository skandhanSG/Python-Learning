def is_pri(number):
    num = int(number / 2)+1
    if number > 1:
        for i in range(2,num):
            if ((number % i )==0):
                return False
        return True
            

number = int(input("Enter a Number: "))
if is_pri(number):
    print(number,  "is a prime number")
else:
    print(number, "is not  prime")    
