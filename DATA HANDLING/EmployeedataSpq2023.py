import csv
def ADD():
    f = open("record.csv", "w")
    writer = csv.writer(f)
    writer.writerow(["empid","name","mobile"])
    n = int(input("How many employees data you want to add :"))
    for i in range(n):
       empid = input("Enter employee id : ")
       name = input("Enter name of employee :")
       mobile = float(input("Enter the salary of employee :"))
       employeedata = [empid,name,mobile]
       writer.writerow(employeedata)
    f.close()
def COUNTR() :
    f = open("record.csv", "r")
    reader = csv.reader(f)
    next(reader) # to not read the Header row
    count = 0
    for i in reader:
        count = count + 1
    print("No of records present in csv file is : ", count)
ADD()
COUNTR()




 
    

