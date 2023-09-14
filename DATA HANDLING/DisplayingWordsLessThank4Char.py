def DISPLAYWORDS():
    count = 0 
    file = open("Story.txt", "r")
    check = file.read()
    words = check.split() # it will split in words so it will be easy to check directly..
    print(words)
    for i in words:
        if len(i)<4:
            print(i)
    file.close()
DISPLAYWORDS()