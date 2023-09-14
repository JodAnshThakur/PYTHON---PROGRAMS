def changevalnum(M,N):
    for i in range(N):
      if M[i]%5 == 0 :
        M[i] //= 5
      if M[i]%3 ==0: #Here the value of the m[i] will be the new value as evaluated in the previous loop
         M[i] //= 3
L = [25,8,75,12]
changevalnum(L,4)
for i in L:
    print(i, end="#")