def simple_interest(p,r=0.10,t =2) :
    return p*r*t

p = float(input("Enter the amount :"))
print("The simple interest with the deafult value is:")
si1 = simple_interest(p)
print("Rs:",si1)
r = float(input("Enter the rate of interest:"))
t = float(input("Enter the time of interest :"))
print("The rate of interst with the provided value is:")
s12 = simple_interest(p,r,t)
print("Rs:", s12/100)