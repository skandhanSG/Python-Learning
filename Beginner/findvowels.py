set1 = "aeiouAEIOU"

def vowelcounter(inputvalue):
    n = 0 
    print(set1)
    for char in inputvalue:
        print(char)
        if char in set1:
            print(char)
            n = n + 1
    return n

inputvalue =(input("enter the word or sentance you need to find the vowels: "))
print("the count of vowels in this is :  ",vowelcounter(inputvalue))       