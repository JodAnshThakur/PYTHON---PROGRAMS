def overlapping(l1,l2):
    len1=len(l1)
    len2 = len(l2)
    for i in range(len1):
        for j in range(len2):
            if l1[i] == l2[j] :
                return True
            else:
                return False
f =overlapping([10,20,30,50],[10,40])
print(f)
