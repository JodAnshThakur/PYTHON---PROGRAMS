#Adding those value of thew list which are at the odd position..
sum = 0
def EvenSum(Numbers):
    for i  in range (len(Numbers)):
        global sum
        if i%2 !=0:
            sum += Numbers[i]
    print(sum)
EvenSum([1,2,3,4,5,6])