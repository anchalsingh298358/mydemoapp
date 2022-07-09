class Library:
    def __init__(self,books,libname):
        self.books = books
        self.name = libname
        self.lbooks = {}
    def display(self):
        i = 1
        print(f"\nBooks That are available in {self.name} Library are -:")
        for book in self.books:
            print(f" {i}.{book} ")
            i += 1

    def lendbook(self):
        username = input("Enter Your Name : ")

        bkname = input("\nEnter name of book you want to lend : ")
        if bkname in self.books:
            self.books.pop(self.books.index(bkname))
            self.lbooks[bkname] = username

            print("\nThanks for lending , pls return it within a week")
        elif bkname in self.lbooks.keys():
            print(f"{self.lbooks[bkname]} had lended {bkname} book earlier")
        else:
            print("Sorry Books not available")

    def addbook(self):
        bookname = input("Name of the  book you want to add : ")
        if bookname not in self.books:
            self.books.append(bookname)

        else:
            print("We already have this book , Thanks for your concern")

        l = input("Want to add another book : ")
        if  l == "y" or l == "yes":
            self.addbook()



    def returning(self):
        usrname = input("Your Name : ")
        bokname = input("Name of Book to return : ")
        if bokname in self.lbooks.keys():
            del self.lbooks[bokname]
            print("Thanks for returning in Time")
        elif bokname in  self.books:
            print("You have returned it already")
        else:
            print("We didnot lend you anybook")


list = ["English","Chemistry","Maths","Hindi","Skt","Bio"]
obj = Library(list,"Python & Coder")
print(f"\t\t\t\t----Welcome to {obj.name} Library---- ")
print("Enter--> \n D for Displaying Books in Library \n L for lending any book \n A for adding books \n R for returning")

key = input("What you want to Do : ")

while 1:
    if key == 'd' or key == 'D':
        obj.display()
        key = input(" How can we help you (D/L/A/R): ")

    if key == 'l' or key == 'L':
        obj.lendbook()
        key = input(" How can we help you (D/L/A/R): ")

    if key == 'r' or key == 'R':
        obj.returning()

        key = input(" How can we help you (D/L/A/R): ")

    if key == 'a' or key == 'A':
        obj.addbook()
        key = input(" How can we help you (D/L/A/R): ")
    else:
        print("Enter wrong key ! ")
        u = input("Want to exit (y/n) : ")
        if u == "y" or u == "Y":
            break
        else:
            key = input(" How can we help you (D/L/A/R): ")
 

