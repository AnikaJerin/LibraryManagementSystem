class Library:
    def __init__(self,library_name,book_list):
        self.ledata={}
        self.liname= library_name
        self.blist=book_list

    def display_books(self):
        for index,books in enumerate(self.blist,1):
            print (f"{index}:{books}")

    def add_books(self,booksname):
        self.blist.append(booksname)
        self.ledata[booksname] = None
        print("Successfully added")
    def lend_books(self):
        n=1
        dict={}
        keys=list(self.ledata.keys())
        vals=list(self.ledata.values())
        for i in range (n):
            name=input("Enter your name:")
            b=int(input("Enter the number of the book you want to borrow:"))
            if b in self.ledata.values():
                print(f"This book has been borrowed by {keys[vals.index(b)]}")

            else:
                dict[name] = b

                self.ledata.update(dict)
                print("Hope you enjoy the book")

    def return_books(self):
        a=int(input("Enter the number of the book you want to return:"))
        if a in self.ledata.values():
            print(f"Thank you for returning the book")
        else:
            print("This book is already available. No need to return")

books=Library("Enlighten",["Harry potter","The lord of rings"])
print(f"Welcome to our Enlighten Library")
print("Kindly choose an option\n","enter'd' if you want to see the booklist\n","enter 'a' if you want to add a book\n",
      "enter 'q' if you want to exit\n","enter 'l' if you want to lend a book\n","enter 'r' if you want to return a book")


exit= False
while(exit is not True):
    i=input("Options:")
    if i=='q':
        exit=True
        print("Have a good day")
    if i=='d':
        books.display_books()

    elif i=='a':
        i1=input("Which books do you want to add\n")
        books.add_books(i1)
    elif i=='l':

        books.lend_books()
    elif i=='r':
        books.return_books()




