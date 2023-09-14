def LShift(Arr,n):
    L = len(Arr)
    for x in range(0,n): # Here splitting depends on n value as n = 2 therefore two time the lope will 
                          # execute and first two value will be  # send to last...
        y = Arr[0] #Assigning the first value to y to directly print it in last.
        for i  in range(0,L-1):
            Arr[i] = Arr[i+1]
        Arr[L-1] = y
    print(Arr)
Arr = [1,2,3,4,5]
n= 2
LShift(Arr,n)