def COUNTLINES():
    f = open("TESTFILE.TXT","r")
    lines = f.readlines()
    for i in lines:
        if i[0] not in 'AEIOU'or i[0] not in "aeiou" :
            print(i)
COUNTLINES()
