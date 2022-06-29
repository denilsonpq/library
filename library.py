class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrewed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available in or list")

    def addBook(self, returnedbook):
        self.availableBooks.append(returnedbook)
        print("You have returned the book. Thank you!")


class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to berrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book wich you are returning: ")
        self.book = input()
        return self.book


library = Library(['Think and Grow Rick', 'Who Will Cry When You DIe', 'For One More Day'])
customer = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())

    if userChoice == 1:
        Library.displayAvailableBooks()
    elif userChoice == 2:
        requestedBook = customer.requestBook()
        Library.lendBook(requestedBook)
    elif userChoice == 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice == 4:
        exit()
