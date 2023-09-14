# Write a function POP_PUSH(LPop,LPush,N), function should pop out the last N elements of the list LPop 
#and Push them into the list LPush.
def POP_PUSH(LPop,LPush,N):
    if N>len(LPop):
        print("Pop not possible")
    else:
        for i in range(N): #One time only one elemnt is poped thats why N = 2 for last 2 elemets
           val = LPop.pop()
           LPush.append(val)
        print(LPush)
        print(LPop) # After Pop. 
              
LPop = [10,15,20,30]
N = 2
LPush =[]
POP_PUSH(LPop,LPush,N)
