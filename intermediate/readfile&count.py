file_path = "C:/Users/SkandhanSivagnanam/Desktop/practice/python-automate-anything--everything/sample.txt"

with open(file_path,"r") as file:
    data = file.read()

lines = len(data.splitlines())
words = len(data.split())
count = len(data)

print(lines,",",words,",",count,",",data)