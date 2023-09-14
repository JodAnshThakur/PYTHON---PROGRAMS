
def INDEX_LIST(L):
    indexList =[]
    for i in L:
     if i!= 0 :
        indexList.append(L.index(i))
    print(indexList)
h = []
n = int(input("How many elements you want to add to your list : "))
for j in range(n):
 user_list = int(input("Enter the value : "))
 h.append(user_list)
p = INDEX_LIST(h)
            

