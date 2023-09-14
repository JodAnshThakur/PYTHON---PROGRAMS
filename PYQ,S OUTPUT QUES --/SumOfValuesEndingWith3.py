sumu = 0
def SUM3(L): # Here L is formal parameter and this can be an 'identifier'
    sumu = 0
    for i in L :
        if i%10 == 3:
            sumu  =  sumu+i
    print(sumu)
h =[]
n = int(input("How many integer elements you want to add to your list : "))
for j in range(n):
 user_list = int(input("Enter the value : "))
 h.append(user_list)
p = SUM3(h) #Actual parameters and they can be ' variable/value, expression'
            



