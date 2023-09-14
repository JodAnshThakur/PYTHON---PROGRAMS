def Factor(num):
    for i in range(2,num):
        if num%i==0:
            return i
num = int(input(("Enter the number whose factor you want : ")))
i = Factor(num)
print(i)