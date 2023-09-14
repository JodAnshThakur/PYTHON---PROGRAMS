w = ['Elucidate', 'Haughty','pacify','Quip','rapport','Urbane', 'Young','Zenith']

#Defining the PUSH functions to push elements whose length is less then 7 char:
def PUSH(stk,N):
    stk.append(N)

#Defing the POP funtions which will pop the elements form the stk and print them in LIFO order.
def POP(stk):
    return stk.pop()

stk = []
#Checking the cvonditions and call the functions:
for i in w:
    if len(i)<7:
        PUSH(stk,i)
print(stk)

#Checking the condtions for poping the elements
while True:
    if stk!=[]:
        print(POP(stk)),"\t"
    # else:
    #     print("Stack is empty.")

