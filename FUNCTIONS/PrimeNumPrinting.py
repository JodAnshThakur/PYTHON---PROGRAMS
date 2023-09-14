def PrimeNum(n):
    for i in range(2,n):
        if n%i ==0 :
            return False
        else :
            return True
n = input("Enter the number to check: ")
f = PrimeNum(n)
if f==True:
    print("This is a prime number")
else:
    print("This is not a prime number")