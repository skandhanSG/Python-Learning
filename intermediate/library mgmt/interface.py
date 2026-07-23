from store import libbook,racker

rackno = []

count =int(input("Enter the count of rack: "))

for i in range(count):
    rack_no = input("enter rack no")
    rackin = racker(rack_no)

    booker = int(input("Enter the no of book: "))
    for j in range(booker):
        bookname = input("enter book name: ")
        bookprice = float(input("enter the price: "))

        book = libbook(bookname,bookprice)
        rackin.add_book(book)

    rackno.append(rackin)    

print("lib details")

for r in rackno:
    r.display()

    
