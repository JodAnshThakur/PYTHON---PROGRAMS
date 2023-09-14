# Function in python which return the value deleted from the stack.
def POP(Arr):
    if len(Arr) == 0:
        print("Stack is empty.")
    else :
        value = Arr.pop()
        return value
list  = [2,15,10,42,13,87,100,58,0,60]
val = POP(list)
print(val)