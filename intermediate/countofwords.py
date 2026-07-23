import re

# Sentence with punctuation
sentence = input("enter the sentence: ") or "Python is an amazing programming language Python"

# Find all character sequences, ignoring punctuation marks
words = re.findall(r'\w+', sentence)

# Loop through and read each word
for word in words:
    print(word)

i=0
j=0
num=0
num1=0

# Split the sentence into a list of words
words = sentence.split()

print(words)
for word in words:
    num=num+1
    print(word,"-",num)
# Loop through and read each word
for i in range (len(words)):
    
    for j in range (i+1,(len(words))):

        if (words[i]==words[j]):
            print(words[i] ,"=", words[j])
            num1=num1+1
            print(words[j])
            print(num1)
    