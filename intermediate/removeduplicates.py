import numpy as np

def remove_duplicates(value):
    return np.unique(value)

def remove_duplicates2(value):
    return list(set(value))

def remove_duplicates3(value):
    return list(dict.fromkeys(value))

def main():
    value = input("enter the list: ")
    values = value.split(",")
    print("I have 3 logic for you to remove duplicates")
    while True:
        print("1. Logic 1 numpy method")
        print("2. Logic 2 set method")
        print("3. Logic 3 dict.fromkeys method")
        logic = int(input("enter the logic you wish to user: "))
        switch = {
            1: remove_duplicates(values),
            2: remove_duplicates2(values),
            3: remove_duplicates3(values)
        }

        try:
            if logic in switch:
                print(switch[logic])
            else:
                print("invalid choice!")
        except ValueError:
            print("Please enter number")

if __name__ == "__main__":
    main()
                       

