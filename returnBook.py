import bookList
from dateAndTime import getDate,getTime,getRemainingDate
from os import system
import time
from bookList import manageBookList
global bookBorrowedDate
def returnBook():
    while True:
        print("----Returning the book ----\n\n")
        name=str(input("Enter your FullName:"))

        # this block checks book is already returned or not if returned  go to main menu
        # if(os.path.isfile(f'Returned by-${name}.txt')):
        #     system("clear")
        #     file=open(f'Returned by-${name}.txt')
        #     returnedBooks=file.read()
        #     print(returnedBooks)
        #     file.close()
        #     print("\n\n\tBook is Already returned\n")
        #     print("\t\tWait main menu.....")
        #     time.sleep(6)
        #     return
        if(" " in name):
            break        
        print("please enter full name\n")
    try:
        with open(f"Borrowed by-{name}.txt","r") as f:
             date=f.readlines()[4]
             bookBorrowedDate=date.strip().replace("Date:","").split("-")
        with open(f"Borrowed by-{name}.txt","r") as f:
            books=f.read()
            price=0.0
            for i in range(len(bookList.bookname)):
                if(bookList.bookname[i] in books):
                    price+=bookList.bookPrice[i]
            system("clear")        
            print(books)
            print(f"\t\t\t\t\t    ${price}")
    except: 
        system("clear")
        print("Borrowed name is incorrect.Please try again")
        returnBook();

    with open(f'Returned by-${name}.txt',"w") as f:
        f.write("\t\t\tlibrary Book Management \n\n")
        f.write("\t\t\t\tReturned  By "+name+"\n\n")
        f.write(f"\t Date:{getDate()} \t\t Time:{getTime()}\n")

        f.write("S.N \t\t Bookname \t\t AuthorName \t\t cost\n")
        for i in range(len(bookList.bookname)):
            if(bookList.bookname[i] in books):
                f.write(f"{i+1} \t\t ${bookList.bookname[i]} \t\t {bookList.bookwriter[i]} \t\t ${bookList.bookPrice[i]}\n")
                manageBookList(i,bookList.numberOfBookAvailable[i]+1)


        remainingDate=getRemainingDate(bookBorrowedDate)
        if remainingDate < 0 :
            fine=2*abs(remainingDate)
            f.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\tLate days :{str(abs(remainingDate))}\n")
            f.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\tFine: $ {str(fine)}\n")
            price=price+fine
        f.write(f"\n\t\t\t\t\t\t\t\tDay remaining to return book : {remainingDate} days")    
        print(f"Final Total: ${str(price)}\n")
        f.write(f"\t\t\t\t\t\t\t\t\t\t\t\t\tTotal: $ {str(price)}\n")
        time.sleep(4)
