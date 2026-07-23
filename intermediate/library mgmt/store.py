class libbook:
    def __init__(self,bookname, price):
        self.bookname =bookname
        self.price = price

    def display(self):
        print(self.bookname," - ",self.price)

class racker:
    def __init__(self,rackno):
        self.rackno = rackno
        self.bookno =[]
    
    def add_book(self,book):
        self.bookno.append(book)

    def display(self):
        print(f"The rack : {self.rackno}")
        for book in self.bookno:
            book.display()
            print()