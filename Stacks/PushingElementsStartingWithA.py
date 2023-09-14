#Pushing those elements in a stack which satrts with 'A'--
def PUSH(N):
    stk = []
    for i in N:
       if 'A' in i: # Chekcing the presence of A in List.
        stk.append(i)
    return stk

#Poping the values store
def POP(stk):
 for i in range(len(stk)):
    if stk!=[]:
      print(stk.pop())
 else :
       print("Empty")

N = ['ANKITA', 'NITISH', 'ANSHoP','DIMPLE','HARKIRAT']
stk =PUSH(N)
print(stk)
POP(stk)







