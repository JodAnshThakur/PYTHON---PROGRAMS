def EvenSum(Numbers) :
    sum = 0
    for i in range(len(Numbers)) :
        if Numbers[i] % 2 == 0:
            sum = sum + Numbers[i]
            return 
EvenSum([10,20,30])
print()
