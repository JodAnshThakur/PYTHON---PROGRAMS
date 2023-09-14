''' A binary file "PLANTS.dat" has structure(ID, NAME, PRICE).
[1] -  Write the definiton of a function WRITEREC() in python, to input data for records from the user  and write
them to file PLANTS.dat,

[2] - Write  the definition of a function SHOWHIGH() in python, which reads the records of PLANTS.dat and display
those records for which the PRICE is less then 500'''

#-------------------------------------------------------------------------------------------------------------------#

# [1] : 
import pickle
def WRITEREC():
 file  = open("PLANTS.dat", "wb")
 n = int(input("How many records you want to enter : "))
 for i in range(n) :
    ID = int(input("Enter the plant  Id : "))
    NAME = input("Enter the plant name : ")
    PRICE = float(input("Enter the plant price : "))
    DATA = [ID, NAME, PRICE]
    pickle.dump(DATA,file) # Function to directly insert the values in binary file.
 file.close()

  # [2] : 
def SHOWHIGH():
  file  = open("PLANTS.dat", "rb")
  for i in file :
   DATA = pickle.load(file)
   if DATA[2] <500 :
     print(DATA[1])
  file.close()




WRITEREC()
SHOWHIGH()





