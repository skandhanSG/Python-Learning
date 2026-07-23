import numpy as np
num = input("Enter the list of numbers : ")
num0 = [int(x.strip()) for x in num.split(",")]
num1 = np.unique(num0)
num2 = [int(x) for x in sorted(num1,reverse=True)]
print("The second largest number is : ",num2[1])


print("logic 2")
num3 = list(set(int(x.strip()) for x in num.split(",")))
num3.sort(reverse=True)
print("The Second largest number is : ",num3[1])
