def report():
    student1 = {
        "sub1" : 100,
        "sub2" : 90,
        "sub3" : 100
    }

    total = sum(student1.values())
    print(f"total marks are: {total}")

    avg = total / len(student1)
    print(f"avg {round(avg,1)}")

    for sub, marks in student1.items():
        print(f"{sub} : {marks}")

    max_mark = max(student1.values())
    print(max_mark)
    max_sub = max(student1, key=student1.get)
    print(f"max marks are in {max_sub} : {max_mark}")   

    if avg >= 90:
        return "A"
    else:
        return "B"

def main():
    print(f"Grade: {report()}")

main()