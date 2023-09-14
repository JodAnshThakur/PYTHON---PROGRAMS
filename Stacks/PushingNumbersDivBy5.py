def PUSH(Arr):
    stk = []
    for i in Arr:
        if i % 5 == 0:
            stk.append(i)
    if len(stk) == 0:
        print("Empty stack bitch: ")
    else :
        print(stk)

N = [2,15,10,42,13,87,100,58,0,60]
PUSH(N)



