import csv
def add():
    f = open("furdata.csv", "w")
    writer = csv.writer(f)
    writer.writerow(["fid","fname","fprice"])
    n = int(input("How many Furniture record you want to add :"))
    for i in range(n):
       fid = input("Enter furniture id : ")
       fname = input("Enter name of furniture :")
       fprice = float(input("Enter the furniture price :"))
       furniture_record = [fid,fname,fprice]
       writer.writerow(furniture_record)
    f.close()
def search() :
    f = open("furdata.csv", "r")
    reader = csv.reader(f)
    next(reader) # to not read the Header row
    for  i in reader:
        if int(i[2])>10000:
            print(i)
        else:
            print("No record found.")
add()
search()




 