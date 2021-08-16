from os import system
import os
import time
from dateAndTime import getDate,getTime
import bookList
from bookList import manageBookList

books=bookList.bookname
bookWriter=bookList.bookwriter
bookQuantity=bookList.numberOfBookAvailable
def selectBook(i):
    if(bookQuantity[i-1]<=0):
        return 0
    bookQuantity[i-1]-=1
    manageBookList(i-1,bookQuantity[i-1])
    return f" {books[i-1]} \t\t\t\t{bookWriter[i-1]} \n"

def addBook(name,bookSelect):
    with open(f"Borrowed by-{name}.txt","a") as f:
        file=open(f"Borrowed by-{name}.txt")
        borrowedBook=file.read()
        file.close()
        if(books[bookSelect-1] in borrowedBook):
            print("You cannot borrowed this book.You already have this book")
        else: 
            f.write(selectBook(bookSelect))


def borrowBook():
    success=True
    loop=False
    while True:
        print("----Book Borrowing -----\n\n")
        name=str(input("Enter Your Full Name :-"))
        
        #this block checks whether same person again borrow book or not ...if same person then go to main menu 
        #
        # if(os.path.isfile(f'Borrowed by-{name}.txt')):
        #     print("Name already exist...\n ")
        #     print("\t\tWait main menu.....")
        #     time.sleep(3)
        #     system("clear")
        #     borrowBook()
        if(" "  in name):
            break          
        print("Enter name in alphate Or Enter full name")

        

    while success:
        count=0
        system("clear")
        print("Please Select a option Below:\n")
        
        for i in range(len(books)):
            count+=1
            print(f"Enter {i+1} to borrow {books[i]}")
        try:    
            bookSelect=int(input("Enter the number:"))
            if(bookSelect >=1 and bookSelect<=(len(books))):
                isBookAvailabe=selectBook(bookSelect)
                if(isBookAvailabe==0):
                    print("Book is not available")
                else: 
                    if(not loop): 
                        with open(f"Borrowed by-{name}.txt","w") as f:
                            f.write("\n\t\tlibrary Book Management \n")
                            f.write("\n\tBorrowed By "+name+"\n")
                            f.write(f"\t Date:{getDate()} \t\t Time:{getTime()}\n\n")
                            f.write(" Bookname \t\t\t\t\t\t AuthorName\n")
                            f.write(str(selectBook(bookSelect)))
                    else:
                        addBook(name,bookSelect)
                        loop=False       
            addAnotherBook=input("Do You want to add another borrowBook?[Y/N]:-")
            addAnotherBook.lower()
            if(addAnotherBook=="y"):
                loop=True;
            else:
                print("Thanks for borrowing books\n")
                success=False;
        except ValueError:
            print(" ")
        


