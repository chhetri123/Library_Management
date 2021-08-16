def availableBooks():
    global bookname
    global bookwriter
    global numberOfBookAvailable
    global bookPrice
    bookname=[]
    bookwriter=[]
    numberOfBookAvailable=[]
    bookPrice=[]

    with open("booklist.txt","r") as f:
        bookDetails=f.readline()
        while bookDetails:
            bookDetails = bookDetails.split(",")
            bookname.append(bookDetails[0])
            bookwriter.append(bookDetails[1])
            numberOfBookAvailable.append(int(bookDetails[2]))
            bookPrice.append(float(bookDetails[3].strip('$"\n"')))
            bookDetails=f.readline()
availableBooks()
def displayBook():
    with open("booklist.txt","r") as f:
        bookDetails=f.read()
        print(bookDetails)

def manageBookList(i,numberOfBook):
    with open("booklist.txt","w+") as f:
        numberOfBookAvailable[i]=numberOfBook
        for number in range(len(bookname)):
            f.write(f"{bookname[number]},{bookwriter[number]},{numberOfBookAvailable[number]},${bookPrice[number]}\n")
            

