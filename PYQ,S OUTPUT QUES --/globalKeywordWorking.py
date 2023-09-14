test = 100
def global_check(a):
    global test
    test = 200
    pp = test*a
    print(test)
    print(pp)
s  = global_check(10)
print(test) # print the global value of a i.e, inside the function block [ a = 200]