def FindOut(Names,HisName):
    for i in range (len(Names)):
         if Names[i] == HisName:
          print(HisName,'at', i)
HisName = "Tarun"
Names = ["Arun","Raj","Tarun","Kanika"]
FindOut(Names,HisName)