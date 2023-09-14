#Pushing and poping those elements which are divisble by 5 and 3 .
def Only3_5(stk,N):
    stk.append(N)

def POP3_5(stk):
    for j in range(len(stk)):
        if stk != []:
            print(stk.pop())
    else:
            print("Stack empty")

list = [10,6,14,18,30]
stk =[]
#Checking conditions for pushinng the elements in the stack
for i in list:
    if i%3 == 0 or i%5 == 0:
        Only3_5(stk,i) 
print(stk)
POP3_5(stk)