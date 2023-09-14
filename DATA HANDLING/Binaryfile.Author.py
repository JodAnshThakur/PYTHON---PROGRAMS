import pickle
def CreateFile():
    n = int(input("How many records you want to add : "))
    for i in range(n):
        f = open("Book.dat","wb")
        BookNo = int(input("Enter the number of the book :"))
        Book_Name = input("Enter the name of the book :")
        Author = input("Enter the author name of the book :")
        Price = float(input("Enter the price of the book :"))
        data = [BookNo, Book_Name, Author, Price]
        pickle.dump(data,f)
        f.close()

def CountRec(Author):
    f = open("Book.dat","rb")
    read = pickle.load(f)
    while True:
        if read[2] == Author :
            print(read)
CreateFile()
check_au_name = input("Enter the name of the author you want to check: ")
CountRec(check_au_name)
