def ETCount():
    f = open("TESTFILE2.TXT", "r")
    words = f.read()
    count_Tt = 0 
    count_Ee = 0
    for i in words:
        if i == 'T' or i == 't':
            count_Tt +=1
        if i == 'E' or i == 'e':
            count_Ee +=1
    print("The number of E or e : ", count_Ee)
    print("The number of T or t : ", count_Tt)
ETCount()