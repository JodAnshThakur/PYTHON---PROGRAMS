def MESEARCH(STATES):
    for i in STATES :
        for j in i:
            if j[0]=='M':
                print(i)
MESEARCH(["MP","UP","WB","TN","MH","MZ","DL","BH","RJ","HR"])
