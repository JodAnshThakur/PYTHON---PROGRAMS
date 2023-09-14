def Display(str) :
    m=""
    for i in range(0, len(str)):
        if(str[i].isupper()):
         m = m+str[i].lower()
        elif str[i].islower():
            m = m+str[i].upper()
        else:
            if i%2 == 0:
              m = m+str[i-1]
            else:
              m = m+"#"
    print(m)
Display('Fun£Python3.0')
           