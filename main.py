from os import system

from bookList import availableBooks,displayBook
from borrowBook import borrowBook
from returnBook import returnBook

def main():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("1. To Display")
        print("2. To Borrow a book")
        print("3. To return a book")
        print("4. To exit\n\n")
        try:
            a=int(input("Select a choice from 1-4: "))
            if(a==1): 
                system("clear")
                displayBook()  
            elif(a==2):
                system("clear")
                availableBooks()
                borrowBook()
                system("clear")
            elif(a==3):
                system("clear")
                availableBooks()
                returnBook()
                system("clear")
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            system("clear")
            print("Please input as suggested.")
main()