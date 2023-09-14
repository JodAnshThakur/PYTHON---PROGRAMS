# Doubling and adding the odd values..

def DoubletheOdd(Nums):
    sum = 0
    for i in Nums:
        if i%2 !=0:
            sum += (i*2) 
    print(sum)
Nums = [25,24,35,20,32,41]
DoubletheOdd(Nums)