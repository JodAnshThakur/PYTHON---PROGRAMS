x = 3
def myfunc():
    global x 
    x+=2
    print(x)
print(x)
myfunc()
print(x)