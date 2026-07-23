def rev(string):
    return string[::-1]

string = str(input("enter the string to reverse: "))
print("Reverse of the given string is : " ,rev(string))

print ("logic - 2")

def revlogic2(string2):
    newstring = ""
    for char in string2:
        newstring = char + newstring
    return newstring


string2 =str(input("enter the string for logic 2: "))
print("new logic reverse is : ",revlogic2(string2))