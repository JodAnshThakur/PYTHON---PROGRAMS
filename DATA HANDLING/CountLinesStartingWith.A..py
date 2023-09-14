# Program to count the number of lines which are starting with letter 'A' #
def Count_Lines():
    count = 0 
    file = open("F:\CS ROAD TO 98+\DATA HANDLING\Countlines.TXT", "r")
    check = file.readlines()
    for i in check:
        if i[0] == 'A':
            count = count+1
            print(i)
    print(count)
    file.close()
Count_Lines()