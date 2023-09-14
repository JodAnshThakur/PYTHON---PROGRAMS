def CountMe_My():
    f = open("STORY1.TXT","r")
    data = f.read()
    count = 0
    words = data.split() # Split every single words in the text file
    print(words)
    for i in words:
        if  i == 'Me' or i == "My":
            count += 1
    print("Count of Me/My in file : ",count)
CountMe_My()
