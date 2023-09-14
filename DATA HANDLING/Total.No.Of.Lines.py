def Count_line():
    file = open("DATA HANDLING\Testing_Text_File..TXT","r+") 
#-----------------------------------------------------------------------------------------#
    # readline = file.readline() #  
    # print(readline) 
    # no_char = len(readline)  # This will  give the total no. of char in the first line text file.
    # print("Total number of Words in first line : ", no_char)
#-----------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------#
    # readline = file.read() 
    # print(readline) 
    # no_char = len(readline)  # This will give the total no of char in the of the text file. 
    # print("Total number of Character in file : ", no_char)
#-----------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------#
    readline = file.readlines() 
    print(readline) 
    no_lines= len(readline)  # This will  give the total no. of lines of the text file. 
    print("Total number of Lines in file : ", no_lines)
#-----------------------------------------------------------------------------------------#
    file.close()

Count_line()
