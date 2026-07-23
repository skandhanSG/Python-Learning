def is_palindrome(word):
    num = len(word)
    for i in range(num):
        if word[i] != word[num - i -1]:
            return False
    return True 


def main():
        word = input("Enter the word for checking: ")
        if is_palindrome(word):
            print(word, "is a palindrome")
        else:   
            print(word, "is not a palindrome")

main()
