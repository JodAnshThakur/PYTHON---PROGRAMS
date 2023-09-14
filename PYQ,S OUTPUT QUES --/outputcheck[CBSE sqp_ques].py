value = 50
def display(N):
    global value
    value  = 25
    if N%7==0:
        value = value = N
    else:
        value  = value-N
print(value, end='#')
display(20)
print(value)